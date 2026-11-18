# 24_the_database_administrator_KNOWLEDGE.md
**Role:** Principal Database Administrator — Hector Ramirez
**Purpose:** Offline, high-density practitioner brief for Database Engine Internals, Query Optimization, Transaction Isolation, Storage Structures, and HA/DR.
**Primary Academic & Industry Anchors:** Abraham Silberschatz, Henry F. Korth, S. Sudarshan (2019), *Database System Concepts* (7th ed.); C.J. Date (2003), *An Introduction to Database Systems*; Baron Schwartz et al., *High Performance Database Systems*.

---

## 1. Transaction Concurrency & ACID Guarantees (Silberschatz et al., 2019)
*   **ACID Fundamentals:**
    *   *Atomicity:* All operations in a transaction complete successfully, or all are rolled back. Maintained via Write-Ahead Logging (WAL / undo logs).
    *   *Consistency:* Database moves from one valid state satisfying all constraints (foreign keys, uniqueness, check constraints) to another.
    *   *Isolation:* Concurrent execution leaves the system in the same state as if transactions executed serially.
    *   *Durability:* Once committed, updates survive system crashes. Guaranteed by flushing WAL to disk before returning commit success.
*   **ANSI SQL Isolation Levels & Concurrency Phenomena:**
    | Isolation Level | Dirty Read | Non-Repeatable Read | Phantom Read | Serialization Anomaly |
    |---|---|---|---|---|
    | **Read Uncommitted** | Possible | Possible | Possible | Possible |
    | **Read Committed** (Postgres/Oracle default) | **Prevented** | Possible | Possible | Possible |
    | **Repeatable Read** (MySQL InnoDB default) | **Prevented** | **Prevented** | Possible (prevented in Postgres MVCC) | Possible |
    | **Serializable** | **Prevented** | **Prevented** | **Prevented** | **Prevented** |
*   **Multi-Version Concurrency Control (MVCC):**
    *   Readers do not block writers, and writers do not block readers.
    *   Each row has invisible system attributes: `xmin` (creating transaction ID) and `xmax` (deleting transaction ID).
    *   *Table Bloat & Vacuuming:* In PostgreSQL, `UPDATE` is physically implemented as an `INSERT` of a new tuple and marking the old tuple as dead (`xmax = current_tx`). Dead tuples accumulate and cause table bloat until collected by `VACUUM`. Tune `autovacuum_vacuum_scale_factor` (e.g. to $0.05$ on large tables).

---

## 2. Physical Storage & Index Internals
*   **B-Tree & B+ Tree Indexes:**
    *   Balanced tree structure with $O(\log N)$ lookup, insert, and delete complexity.
    *   *B+ Tree Property:* Internal nodes contain only routing keys; all actual data pointers/row IDs reside in leaf nodes, which are linked as a doubly-linked list. Ideal for both point lookups and range scans.
    *   *Clustered vs. Non-Clustered:* Clustered index physically orders table data on disk based on index key (only 1 per table); non-clustered index stores index key with a pointer (Row ID or Primary Key) to the heap tuple.
    *   *Covering Index (`INCLUDE`):*
        `CREATE INDEX idx_orders_customer ON orders (customer_id) INCLUDE (order_date, total_amount);`
        Allows index-only scans: the engine fulfills the entire query directly from the leaf pages without accessing the heap table.
*   **Log-Structured Merge (LSM) Trees (RocksDB, Cassandra, SQLite4):**
    *   Optimized for high-throughput write workloads.
    *   Writes append sequentially to an in-memory `MemTable` and a WAL log. When full, flushed to disk as immutable sorted string tables (`SSTables`).
    *   Background compaction merges overlapping SSTables. High write performance at the expense of read amplification.
*   **Specialized Indexes:**
    *   *GIN (Generalized Inverted Index):* Inverted list mapping elements to row IDs. Essential for full-text search, arrays, and PostgreSQL `JSONB` path queries (`@>`).
    *   *BRIN (Block Range Index):* Stores min/max values for ranges of physical disk pages (e.g. 128 pages). Extremely lightweight for massive append-only time-series tables physically ordered by timestamp.

---

## 3. Query Optimization & Plan Analysis
*   **Cost-Based Optimizer (CBO) Mechanics:** Evaluates candidate execution plans and selects the lowest estimated cost in I/O disk page fetches and CPU tuple evaluations.
*   **Execution Plan Analysis (`EXPLAIN (ANALYZE, BUFFERS)`):**
    *   *Sequential Scan (Seq Scan):* Reads every page of the table. Optimal for small tables or queries retrieving $>20-30\%$ of rows; disastrous for point lookups on million-row tables.
    *   *Index Scan:* Traverses B-tree to leaf node and fetches matching heap tuples one by one.
    *   *Index Only Scan:* Fetches data entirely from the index leaf nodes (requires heap visibility map up-to-date via vacuuming).
    *   *Bitmap Index Scan:* Builds a memory bitmap of matching physical page addresses, then reads heap pages sequentially.
*   **Join Execution Algorithms:**
    *   *Nested Loop Join:* For each row in outer table, probes inner table index. Optimal when outer table is tiny and inner table is indexed.
    *   *Hash Join:* Builds in-memory hash table on smaller table, then streams larger table probing the hash table. Optimal for large, unsorted, unindexed equality joins.
    *   *Merge Join:* Both inputs must be sorted on join key; scans both in parallel like a zipper. Optimal for large sorted inputs.
*   **Sargable Query Design (Search Argument Able):**
    *   *Anti-Pattern (Non-sargable):* `WHERE UPPER(email) = 'USER@EXAMPLE.COM'` (disables B-tree index on `email`).
    *   *Remedy:* Use expression index (`CREATE INDEX ON users (UPPER(email))`) or normalize data on insert.
    *   *Anti-Pattern (Wildcard prefix):* `WHERE name LIKE '%tech'` (forces full table scan; use trigram GIN index `pg_trgm`).

---

## 4. High Availability (HA), Replication & Disaster Recovery
*   **Physical Streaming Replication:**
    *   *Asynchronous:* Primary writes to WAL, returns success to client, then streams WAL to standby. Standby can lag slightly; risk of minimal data loss on sudden primary death.
    *   *Synchronous:* Primary waits for at least one standby to write WAL to disk before returning success to client. Zero data loss ($RPO = 0$), but write latency increases with network RTT.
*   **Logical Replication:**
    *   Pub/Sub model streaming decoded row changes. Enables cross-major-version upgrades, zero-downtime migrations, and selective table replication.
*   **Backup Protocols & Point-In-Time Recovery (PITR):**
    *   *Base Backup:* Periodic physical snapshot of all data files (`pg_basebackup`).
    *   *Continuous WAL Archiving:* Every completed WAL segment ($16\text{MB}$) is immediately shipped to durable remote object storage (S3).
    *   *PITR Restoration:* Restore base backup, then replay WAL logs up to the exact target microsecond before accidental data truncation:
        `recovery_target_time = '2026-09-11 14:22:05-07'`
*   **RTO & RPO Definitions:**
    *   *Recovery Time Objective (RTO):* Maximum acceptable duration of outage before system is restored.
    *   *Recovery Point Objective (RPO):* Maximum acceptable data loss duration measured in time (e.g. maximum 5 seconds of lost transactions).

---

## 5. Enterprise AS/400 IBM DB2 Operations & Heritage
*   **IBM i DB2 Architecture:** Single-level storage architecture where disk and RAM are addressed as one virtual memory space.
*   **Physical Files (PF) vs. Logical Files (LF):**
    *   *Physical File (PF):* The actual data table containing data records.
    *   *Logical File (LF):* Equivalent to an indexed view or access path. An LF defines an access path (index key sequence) and record selection/omission criteria without duplicating the physical data.
*   **Journals & Receivers (AS/400 Audit Trail):**
    *   *Journal:* Object that coordinates transaction logging.
    *   *Journal Receiver:* Physical storage object where before-images and after-images of data records are written. Crucial for enterprise compliance, transaction recovery, and CDC streaming into modern analytics.
