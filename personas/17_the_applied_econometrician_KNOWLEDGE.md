# 17_the_applied_econometrician_KNOWLEDGE.md
**Extracted from NotebookLM:** ICASSSD Research School and AI + MGMT580 Business Analytics
**Purpose:** Offline, high-density practitioner brief for The Applied Econometrician.
**Version:** 2.9 (v2.9)

---

## 1. The Core Frameworks
*   **Creswell's Quantitative Research Designs (Creswell, 2014):**
    *   *Experimental Designs:* Investigate if a treatment affects an outcome. Includes **True Experiments** (with randomized subject assignment) and **Quasi-Experiments** (with non-randomized assignment, e.g., using natural shocks/threshold cutoffs).
    *   *Nonexperimental Designs:* **Surveys** providing numeric descriptions of trends, opinions, or attitudes using a sample. Focuses on construct validity, scale reliability (Cronbach's alpha), and mitigating selection bias.
*   **Evidence-Based Management Levels of Evidence (Barends et al., 2014):**
    *   *Level A (Highest Validity):* Randomized controlled trials with a pre-test. Best for mitigating internal validity threats and proving causality.
    *   *Level B:* Controlled studies without randomization, but with a pre-test (e.g., matching or quasi-experiments with baseline controls).
    *   *Level C:* Controlled studies without a pre-test (post-test only) or uncontrolled studies with a pre-test.
    *   *Level D (Lowest Validity):* Uncontrolled studies without a pre-test (cross-sectional surveys, case studies, qualitative interviews).
*   **Influence Charts (Powell & Baker, 2016):**
    *   Visual diagrams constructed right-to-left used during the formulation phase to bridge the gap between an unstructured problem and a formal mathematical model.
    *   *Octagon/Hexagon:* Represents the objective/outcome variable (measures success).
    *   *Rectangle:* Represents the decision variable (directly controlled by the manager).
    *   *Triangle:* Represents a fixed input parameter (outside immediate control).
    *   *Single Circle:* Represents a general variable (intermediate calculation).
    *   *Double Circle:* Represents a random variable or parameter of uncertainty.
*   **Spreadsheet Engineering Principles (Powell & Baker, 2016):**
    *   A set of design guidelines to eliminate logic errors and operational risks. Key rules: sketch the layout first; isolate input parameters from formulas; design modularly (separate Inputs, Decisions, Calculations, Outputs); and use self-documenting formulas and cell labels.
*   **Model Analysis Methods (Powell & Baker, 2016):**
    *   *Base-Case Analysis:* Testing the model with the most likely parameters.
    *   *What-If Analysis:* Varying inputs to observe impact on outputs (utilizing Scenario Manager and Tornado Charts).
    *   *Breakeven Analysis:* Finding the value of a decision variable that yields zero profit.
    *   *Optimization:* Finding the decision values that maximize or minimize the objective.
    *   *Monte Carlo Simulation:* Replacing fixed parameters with probability distributions.
*   **Rotering's Objective Value vs. Subjective Utility (ENL Framework):**
    *   *Subjective Utility Critique:* Neoclassical welfare functions rely on revealed preferences ($WTP$). In ecological overshoot, $WTP$ prices luxury polluters high and biophysical survival low.
    *   *Ruskinian Objective Value:* $\text{Value} \equiv \Delta \text{Physical Health} > 0$. Cost is $\Delta \text{Physical Health} < 0$ (toxic loading, labor morbidity).
    *   *The 6 Hard Physical Outcome Constraints:* Outputs, Quantities, Wastes, Resources, Habitat, Population. Must be modeled as hard physical upper bounds rather than flexible monetary shadow prices.

---

## 2. The Methodologies & Formulas
*   **Heat Shock Impact Formulas:** Used to quantify the economic exposure of firms to local and peer climate events:
    *   **Establishment-Level Own Shock:** $Log(1 + \#Hot Days_{c,t})$
    *   **Establishment-Level Peer Shock:** $Log(1 + \#Hot Days, Other_{f,c,t})$ where $\#Hot Days, Other_{f,c,t} = \sum_{c' \neq c} \frac{Employment_{f,c',t-2}}{Employment_{f,c,t-2}} \times \#Hot Days_{c',t}$
    *   **County-Level Peer Shock:** $Log(1 + \sum_{f} \frac{Employment_{f,c,t-2}}{Employment_{c,t-2}} \times \#Hot Days, Other_{f,c,t})$
*   **Influence Chart Decomposition Method:**
    1. Draw the final objective (Octagon) on the far right.
    2. Decompose the objective into its immediate, independent sub-variables (Circles).
    3. Work backward (leftward) for each variable, asking "What do I need to calculate this?" until you reach decisions (Rectangles) and parameters (Triangles/Double Circles).

---

## 3. The Empirical Evidence
*   **Invivo Diagnostics R&D Allocation:** Illustrates the six-stage problem-solving process. The firm explored the mess of expiring patents, gathered generic market data, defined their problem as reducing time-to-market for pipeline drugs, brainstormed shifting budgets, and evaluated options using NPV.
*   **Netscape Corporate Valuation:** Demonstrates Monte Carlo simulation in Excel, where revenue growth rates and R&D costs were modeled as normal probability distributions to generate a probabilistic range of Netscape's 10-year free cash flows and valuation.
*   **Macroeconomic Heat Shock Reallocation:** Within 3 years of a heat shock, employment growth in single-location firms declines by 1.05 percentage points. Conversely, multi-location firms increase employment and job postings in unaffected peer locations (shifting jobs from Phoenix to Seattle). Roughly 75% of employment lost by heat-exposed firms is reabsorbed elsewhere in the economy via this network.

---

## 4. The Practitioner's Playbook
*   **Apply the Influence Chart Before Build:**
    *   Never open Excel without drawing the influence chart first.
    *   Draw right-to-left: start with the Octagon objective and trace calculations back to input parameters. Ensure no variable appears more than once to prevent circular references.
*   **Modularize the Spreadsheet Layout:**
    *   Organize spreadsheets into distinct, labeled blocks: (a) Input Parameters (Triangles), (b) Strategic Decisions (Rectangles), (c) Calculations (Circles), and (d) Final Outcomes (Octagons).
*   **Run Tornado Charts for Sensitivity:**
    *   Before recommending a strategic path, run a Tornado analysis to visually rank the sensitivity of the objective relative to each input parameter, focusing management attention on the most volatile drivers.
*   **Layer Theoretical Hunches in Data Selection (Allamraju, 2026):**
    *   Literature reveals default variables, but when standard metrics fail in context, layer in informed judgment to construct custom indicators (e.g. using a weighted real exchange rate instead of standard measures when analyzing currency pressure).
*   **Audit Experimental Reproducibility & SI Data:**
    *   Guarantee full methodological reproducibility. Require systematic research diary logging and isolate bulky mathematical regressions/raw code in the Supplementary Information (SI).

---

## 5. The Red Flags
*   **Hard-Coded Parameters in Formulas:** Embedding raw numbers (e.g., tax rate = 0.3) in calculation cells rather than referencing separate input cells. This makes models rigid and prone to logic errors.
*   **Circular References in Influence Charts:** Allowing arrows to flow both ways or drawing loops in the logic. This indicates flawed problem formulation and prevents mathematical solution.
*   **Chasing Accuracy Over Simplicity:** Building overly complex, multi-variable models that managers cannot interpret. Favor simple, transparent models (the "art of modeling") over bloated simulations unless high-precision data is available.

