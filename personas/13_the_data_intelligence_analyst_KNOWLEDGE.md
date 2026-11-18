# 13_the_data_intelligence_analyst_KNOWLEDGE.md
**Role:** Lead Data Analyst & BI Specialist — Dr. Natasha Kowalski
**Purpose:** Offline, high-density practitioner brief for Exploratory Data Analysis, SQL Analytics, KPI Architecture, and Data Storytelling.

---

## 1. Exploratory Data Analysis (EDA) Protocols (John W. Tukey, 1977)
*   **The 5-Number Summary:** Minimum, First Quartile ($Q_1$), Median ($Q_2$), Third Quartile ($Q_3$), Maximum.
*   **Interquartile Range (IQR):** $\text{IQR} = Q_3 - Q_1$.
    *   *Mild Outliers:* Values outside $[Q_1 - 1.5 \times \text{IQR}, Q_3 + 1.5 \times \text{IQR}]$.
    *   *Extreme Outliers:* Values outside $[Q_1 - 3.0 \times \text{IQR}, Q_3 + 3.0 \times \text{IQR}]$.
*   **Distribution Shape Analysis:**
    *   *Skewness:* Zero for symmetric; positive (right-skewed, mean > median); negative (left-skewed, mean < median). Use log or Box-Cox transformations to normalize right-skewed revenue/duration data.
    *   *Kurtosis:* Excess kurtosis measures tail-heaviness (leptokurtic > 0 vs platykurtic < 0).
*   **Missing Data Imputation Standards:**
    *   *MCAR (Missing Completely at Random):* Listwise deletion acceptable if <5% missing; otherwise median (numerical) or mode (categorical) imputation.
    *   *MAR (Missing at Random):* Predictable from other variables; use regression/KNN imputation or MICE (Multivariate Imputation by Chained Equations).
    *   *MNAR (Missing Not at Random):* Systemic absence (e.g. high-income non-reporting); requires missingness indicator flags.

---

## 2. Tidy Data Principles (Hadley Wickham, 2014)
*   **The Three Core Axioms:**
    1. Each variable must have its own column.
    2. Each observation must have its own row.
    3. Each type of observational unit forms a table.
*   **Data Reshaping Operatives:**
    *   *Pivoting Longer (Un-pivoting / Melting):* Converts column headers that are values (e.g. Q1, Q2, Q3) into a single "Quarter" variable column.
    *   *Pivoting Wider (Spreading):* Moves category levels into column headers for cross-tabulation or dimensional matrix operations.

---

## 3. Advanced Analytical SQL & Cohort Analytics
*   **Window Function Execution Mechanics:** `function() OVER (PARTITION BY ... ORDER BY ... ROWS BETWEEN ...)`
    *   *Ranking:* `ROW_NUMBER()` (unique incremental), `RANK()` (ties share rank, leaves gaps), `DENSE_RANK()` (ties share rank, no gaps).
    *   *Positional:* `LAG(col, n)` / `LEAD(col, n)` for period-over-period growth calculation:
        $$\text{MoM Growth} = \frac{\text{revenue} - \text{LAG}(\text{revenue}, 1)}{\text{LAG}(\text{revenue}, 1)}$$
    *   *Cumulative Windows:* `SUM(sales) OVER (PARTITION BY store ORDER BY date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)`.
*   **Common Table Expressions (CTEs):** Modularized readability over nested subqueries. Recursive CTEs for hierarchical organizational trees, BOM bill-of-materials, or user referral graph traversal.
*   **Cohort Retention Matrix Protocol:**
    *   Group users by acquisition month (`DATE_TRUNC('month', signup_date)`).
    *   Calculate active periods relative to signup: `cohort_index = (activity_year - signup_year)*12 + (activity_month - signup_month)`.
    *   Pivot results to generate the standard triangular cohort retention heatmap.

---

## 4. KPI Architecture & Executive Scorecards
*   **Leading vs. Lagging Indicators:**
    *   *Lagging:* Outputs/results already achieved (e.g., Quarterly Net Revenue, Churn Rate, Total Cost). Accurate but too late to alter.
    *   *Leading:* Input behaviors predictive of future results (e.g., Weekly Active Pipeline, Product Adoption Velocity, Onboarding Time). Actionable in real time.
*   **Balanced Scorecard Framework (Kaplan & Norton):**
    1. *Financial Perspective:* Operating margin, ROIC, cash conversion cycle.
    2. *Customer Perspective:* Customer Acquisition Cost (CAC), Lifetime Value (LTV), LTV/CAC ratio (>3.0 target), Net Promoter Score (NPS).
    3. *Internal Process Perspective:* SLA adherence, deployment frequency, defect rate, inventory turns.
    4. *Learning & Growth Perspective:* Skill certification velocity, retention of critical talent.
*   **Vanity vs. Actionable Metrics (Eric Ries):** If an indicator cannot directly trigger a specific business intervention when it deviates by $\pm 10\%$, it is a vanity metric and must be downgraded.

---

## 5. A/B Testing & Experimentation Analytics
*   **Hypothesis Formulation:** Clearly state null ($H_0$) and alternative ($H_1$) hypotheses.
*   **Sample Size Sizing Formula (Two-Sample Proportions):**
    $$n = \frac{(Z_{\alpha/2} + Z_{\beta})^2 [p_1(1-p_1) + p_2(1-p_2)]}{(p_1 - p_2)^2}$$
    Where $\alpha = 0.05$ ($Z_{\alpha/2} = 1.96$), Statistical Power $1 - \beta = 0.80$ ($Z_{\beta} = 0.84$), and $p_1 - p_2$ is the Minimum Detectable Effect (MDE).
*   **Statistical Significance vs. Practical Significance:** A p-value $< 0.05$ indicates rejection of $H_0$, but effect size and business ROI determine operational rollout. Always monitor guardrail metrics (e.g. latency, unsubscribe rate, server load) during feature A/B tests.

---

## 6. Data Storytelling & Dashboard Ergonomics (Knaflic & Few)
*   **Cole Nussbaumer Knaflic (2015) 6 Core Principles:**
    1. Understand the audience and context (3-minute story vs 10-slide deck).
    2. Choose the right visual display (tables for exact lookups, bar charts for categorical comparisons, line charts for continuous time series, scatter plots for correlation).
    3. Eliminate clutter (remove borders, background grids, redundant labels, 3D effects, and decorative chartjunk).
    4. Leverage preattentive attributes (color, size, weight) deliberately to direct the viewer's eye to the key insight in under 3 seconds.
    5. Think like a designer (affordances, visual hierarchy, consistent color palette).
    6. Tell an executive story with narrative arc (Situation, Complication, Resolution).
*   **Stephen Few Dashboard Rules:** Avoid fragmented multi-screen scrolling; position high-level summary KPIs at top left; provide context-rich sparklines and bullet graphs instead of radial gauges.

---

## IV. Project Data Dictionary & Synthetic Dataset Generation Protocol (Rule 26)

When engaged in project analysis and design, Natasha operationalizes the PDD-STS standard:

### 1. Data Dictionary Attribute Standards (`docs/data_dictionary.md`)
For each entity and field in the project:
1. `Entity & Field`: `PascalCaseEntity.snake_case_field`
2. `Data Type`: PostgreSQL/Universal standard (`UUID`, `VARCHAR(n)`, `INTEGER`, `DECIMAL(p,s)`, `TIMESTAMPTZ`, `JSONB`)
3. `Constraints`: `PK`, `FK`, `NOT NULL`, `UNIQUE`, `CHECK`, `DEFAULT`
4. `Business Description`: Clear plain-English domain meaning
5. `Business Rules & Validation`: Exact bounds, regex patterns, state transitions
6. `Privacy Classification`: `Public`, `Internal`, `Confidential`, `Restricted / PII`
7. `Originating Lineage`: Conversation ID, session date, or user story reference

### 2. Synthetic Dataset Generation Workflow (`data/synthetic/`)
For every conversation in that project:
- **Envelope Metadata:** Header capturing `conversation_id`, `session_date`, `project_name`, `feature_scope`, `personas_involved`, and `edge_cases_included`.
- **Distribution Modeling:** Generate values using realistic operational distributions (Poisson arrivals, Pareto spend, realistic geographic coordinates) rather than repetitive dummy filler.
- **Stress-Testing:** Ensure 15–20% of records represent boundary conditions, threshold breaches, and failure modes explored in the session.
- **Zero PII Mandate:** 100% synthetic generation via deterministic seeds or faker libraries.

### 3. Catalog (Reference Data) & Trilingual Architecture Protocol (Rule 27)
When authoring Data Dictionaries and generating synthetic datasets:
1. **Catalog Best Practices:**
   - Every controlled list (statuses, categories, types, payment methods) must be normalized into a catalog entity (`cat_<name>`).
   - Must include: `catalog_id`, immutable `catalog_code`, explicit `sort_order` integer, `is_active` boolean, `valid_from`/`valid_to` timestamps, and optional `parent_catalog_id`.
2. **Trilingual Baseline (EN / FR / ES):**
   - All catalog entries must provide translations in **English (EN)**, **French (FR)**, and **Spanish (ES)** via relational translation tables or JSONB `i18n` objects.
   - Synthetic data generation must produce realistic localized data across Canada (EN/FR), USA (EN/ES), and Mexico (ES).
