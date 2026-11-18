# 23_the_data_engineer_KNOWLEDGE.md
**Role:** Principal Data Engineer — Tariq Al-Mansoor
**Purpose:** Offline, high-density practitioner brief for Data Pipelines, Lakehouse Architecture, Dimensional Modeling, and Distributed Computing.
**Primary Academic & Industry Anchors:** Joe Reis & Matt Housley (2022), *Fundamentals of Data Engineering*; Martin Kleppmann (2017), *Designing Data-Intensive Applications*; Ralph Kimball & Margy Ross (2013), *The Data Warehouse Toolkit* (3rd ed.).

---

## 1. The Data Engineering Lifecycle (Reis & Housley, 2022)
*   **The 5 Core Stages:**
    1. *Generation:* Operational databases (OLTP), APIs, IoT sensors, application logs, legacy mainframes.
    2. *Storage:* Object storage (S3, ADLS, GCS), block storage, distributed file systems.
    3. *Ingestion:* Batch vs. micro-batch vs. real-time streaming; push vs. pull mechanisms.
    4. *Transformation:* Cleaning, deduplicating, re-casting, joining, aggregating, business logic modeling.
    5. *Serving:* Analytics, BI dashboards, machine learning feature stores, reverse ETL into operational tools.
*   **The Undercurrents (Cross-Cutting):** Security & Privacy, Data Management (lineage, cataloging), DataOps (testing, CI/CD, monitoring), Data Architecture (modularity, decoupling), Orchestration (scheduling, retries), Software Engineering (DRY code, git versioning).

---

## 2. Ingestion & Pipeline Paradigms (Kleppmann, 2017)
*   **ETL (Extract, Transform, Load) vs. ELT (Extract, Load, Transform):**
    *   *ETL:* Legacy approach. Compute occurs in specialized transformation engines before loading to warehouse. Necessary when transforming on-premise or applying strict anonymization before cloud ingress.
    *   *ELT:* Modern Lakehouse standard. Raw data is loaded directly into scalable cloud storage; compute engine (Snowflake, Databricks, BigQuery, dbt) handles transformation in-place via SQL.
*   **Batch vs. Stream Processing:**
    *   *Batch:* Processes bounded datasets on a fixed schedule (hourly/daily). High throughput, high latency.
    *   *Streaming:* Processes unbounded streams of continuous events (Kafka, Flink). Low latency (<1s).
    *   *Event Time vs. Processing Time:* Event time is when the event physically occurred on the client device; processing time is when the pipeline consumed it. Real-time pipelines require **Watermarking** to handle late-arriving data.
    *   *Delivery Guarantees:* At-least-once (can cause duplicates; requires downstream idempotent deduplication) vs. Exactly-once (achieved via transactional producers and idempotent consumer sinks).

---

## 3. The Modern Data Lakehouse & Medallion Architecture
*   **The Three Medallion Layers:**
    *   **Bronze Layer (Raw Landing):**
        *   Append-only, immutable historical landing zone for all raw source data.
        *   Preserves exact source format (JSON, CSV, CDC events) with ingestion timestamps and source file metadata.
    *   **Silver Layer (Cleaned & Conformed):**
        *   Deduplicated, schema-enforced, cleaned, normalized, and validated data.
        *   Addresses missing data, standardizes datetime formats (UTC), and joins lookup tables.
    *   **Gold Layer (Curated Business Marts):**
        *   Business-level aggregation and dimensional star-schema modeling.
        *   Optimized for sub-second analytical reporting, BI dashboards, and ML feature consumption.
*   **Modern Open Table Formats:**
    *   *Delta Lake / Apache Iceberg / Apache Hudi:* Provide ACID transactional guarantees, snapshot isolation, concurrent reads/writes on object storage (Parquet), schema evolution without rewriting data, and Time Travel (querying historical snapshots `FOR SYSTEM_TIME AS OF`).

---

## 4. Dimensional Modeling (Ralph Kimball Standard)
*   **Core Concepts:**
    *   *Fact Tables:* Contain numeric measurements/metrics of a business event (e.g. sales quantity, revenue, transaction duration).
        *   *Additive:* Can be summed across all dimensions (e.g. dollar sales).
        *   *Semi-Additive:* Can be summed across some dimensions but not time (e.g. account balances).
        *   *Non-Additive:* Ratios, unit prices (must average or recompute).
    *   *Dimension Tables:* Contain context attributes describing the "who, what, where, when, why" (e.g. customer name, product category, store location).
*   **Grain Definition Rule:** The first and most critical step in Kimball modeling is declaring the exact business grain of the fact table (e.g. "one row per individual item scanned at a retail point-of-sale checkout").
*   **Slowly Changing Dimensions (SCD):**
    *   *Type 0 (Retain Original):* Never overwritten (e.g. original birthdate).
    *   *Type 1 (Overwrite):* Directly overwrites old value with new; loses historical state.
    *   *Type 2 (Add New Row):* Industry standard for auditability. Adds a new row with `valid_from`, `valid_to`, and `is_current` boolean flag.
    *   *Type 3 (Add New Attribute Column):* Stores previous value in a dedicated column (`previous_address`).
    *   *Type 6 (Hybrid 1+2+3):* Maintains historical rows (Type 2) while updating an attribute across all historical rows (Type 1).

---

## 5. Distributed Processing with Apache Spark
*   **Execution Architecture:** Driver program coordinates Cluster Manager (YARN, K8s) and assigns tasks to Worker Executors.
*   **Catalyst Optimizer & Tungsten Engine:** Optimizes execution plans via logical plan optimization, physical cost modeling, and whole-stage code generation in native bytecode.
*   **Transformations vs. Actions:**
    *   *Transformations (Lazy):* `map()`, `filter()`, `groupBy()`, `join()`. Build an internal Directed Acyclic Graph (DAG) without executing.
    *   *Actions (Eager):* `count()`, `collect()`, `save()`, `show()`. Trigger actual DAG execution.
*   **Performance Bottlenecks & Optimization:**
    *   *Shuffle Optimization:* Shuffling is the costly repartitioning of data across cluster nodes over the network. Minimize shuffles by pre-partitioning on join keys.
    *   *Broadcast Hash Join:* When joining a massive fact table with a small dimension table (<10MB default, tunable), broadcast the small table to all executors to eliminate network shuffles completely:
        `df_fact.join(broadcast(df_dim), "customer_id")`
    *   *Data Skew Mitigation:* When specific partition keys have massive data concentrations (e.g. nulls or celebrity IDs), apply salting (appending random integer keys) to distribute the partition evenly.

---

## 6. Transformation with dbt (data build tool)
*   **Core Philosophy:** Transform data inside the warehouse using software engineering best practices: version control, modular SQL, testing, documentation, and continuous integration.
*   **Model Materialization Strategies:**
    *   `view`: Recomputes on every query. Fast to build, zero storage cost, slow to query.
    *   `table`: Drops and recreates full table. High write compute, fast analytical query.
    *   `incremental`: Only processes new or modified rows since last run using a watermark filter:
        ```sql
        {{ config(materialized='incremental', unique_key='transaction_id') }}
        SELECT * FROM {{ ref('stg_transactions') }}
        {% if is_incremental() %}
          WHERE updated_at > (SELECT MAX(updated_at) FROM {{ this }})
        {% endif %}
        ```
    *   `ephemeral`: Interpolated as a CTE in downstream models; not materialized in warehouse.
*   **Data Quality Testing:**
    *   Generic tests: `unique`, `not_null`, `accepted_values`, `relationships` (foreign key integrity).
    *   Singular SQL tests: Custom queries returning failing records.
