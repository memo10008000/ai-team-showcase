# 02_the_finance_director_KNOWLEDGE.md
**Extracted from NotebookLM:** MGMT560-Finances
**Purpose:** Offline, high-density practitioner brief for the Finance Director.

---

## 1. The Core Frameworks
*   **Finance vs. Accounting:** **Accounting is backward-looking**, focusing on stewardship, accuracy, and historical transactions. **Finance is forward-looking**, focusing on optimizing future cash flows, risk-return trade-offs, and maximizing shareholder value.
*   **Time Value of Money (TVM):** The foundational principle that **a dollar today is worth more than a dollar tomorrow**; it is the basis for capital budgeting, bond pricing, and equity valuation. 
*   **The Goal of the Corporation:** **Shareholder wealth maximization**, which reflects the timing, magnitude, and riskiness of all future cash flows, rather than simple short-term accounting profit maximization.
*   **Capital Structure:** The mix of debt and equity used to finance investments. **Modigliani-Miller (MM)** theorem serves as the benchmark, illustrating that while debt provides a tax shield that increases firm value, excessive debt introduces financial distress.
*   **Working Capital Management:** The strategy of managing current assets (cash, inventory, receivables) and current liabilities to **balance the trade-off between liquidity (survival) and profitability**.
*   **ESG as Financial Risk:** ESG does not measure "goodness"; **it measures the probability of future cash-flow disruptions** (regulatory changes, lawsuits, supply chain failures). Higher ESG risk directly increases a firm's discount rate and lowers firm value.

## 2. The Methodologies & Formulas
*   **Time Value of Money (Compounding & Discounting):**
    *   **Future Value (FV):** $FV = PV \times (1 + r)^n$.
    *   **Present Value (PV):** $PV = \frac{FV}{(1 + r)^n}$.
    *   **Effective Annual Rate (EAR):** Calculated by compounding the periodic rate over the year. Example for daily compounding: $EAR = (1 + \text{daily rate})^{365} - 1$.
*   **Valuation & Capital Budgeting:**
    *   **Project Value (DCF):** $Value = \sum \frac{FCFF_t}{(1 + WACC)^t} + \frac{TV_T}{(1 + WACC)^T}$.
    *   **Free Cash Flow (FCF):** $FCF = EBIT(1 - T) + Depreciation - CapEx - \Delta NWC$.
    *   **Dividend Discount Model (DDM):** $P_0 = \frac{D_1}{k_c - g}$, where growth $g = \text{retention ratio (b)} \times ROE$.
*   **External Financing Requirements (EFR) / Formula Forecasting:**
    *   Used to determine funding needed for growth: $EFR = a \times S \times g - b \times PM \times (1+g) \times S$ (where $a$ is asset intensity, $S$ is sales, $g$ is growth rate, $b$ is retention ratio, and $PM$ is profit margin).
*   **Weighted Average Cost of Capital (WACC) & Hamada WACC Minimization:**
    *   $WACC = w_d k_d(1 - T) + w_s k_s$. WACC is U-shaped. Adding cheap debt lowers it initially due to the tax shield, but excessive debt increases default risk, raising required returns from both lenders ($k_d$) and equity holders ($k_s$).
    *   **Hamada Equation:** Re-levering beta to determine cost of equity at different debt levels: $\beta_L = \beta_U [1 + (1 - T)(D/E)]$.
    *   **Levered Cost of Equity:** $k_s = R_f + \beta_L (R_m - R_f)$.
    *   **Optimal Borrowing:** Triangulated by calculating WACC across a range of D/E ratios (typically 0% to 90% in 10% increments) using the Hamada equation to find the point where WACC is minimized.
*   **Advanced Capital Budgeting Metrics:**
    *   **Profitability Index (PI):** $PI = \frac{\text{PV of Future Cash Flows}}{\text{Initial Investment}} = \frac{\sum_{t=1}^n \frac{CF_t}{(1+WACC)^t}}{CF_0}$. Accept if $PI > 1.0$.
    *   **Discounted Payback Period:** Time $T$ at which $\sum_{t=1}^T \frac{CF_t}{(1+WACC)^t} = CF_0$.
    *   **Net Working Capital Change ($\Delta NWC$):** $\Delta NWC_t = NWC_t - NWC_{t-1}$, where $NWC = \text{Current Assets} - \text{Current Liabilities}$. Incremental increase in NWC represents a cash OUTFLOW; decrease is a cash INFLOW.
*   **Sensitivity & Tornado Analysis Protocol:**
    *   **Sensitivity Range:** Vary key inputs (Discount Rate, Sales Growth, Margins) by $\pm 10\%$, $\pm 20\%$, and $\pm 30\%$ to project the NPV impact.
    *   **Tornado Ranking:** Rank input variables by the absolute size of their impact on NPV from highest to lowest to identify the most sensitive operational leverage points.

## 3. The Empirical Evidence
*   **Valuation Bubbles:** Models fail when assumptions are detached from reality (e.g., growth assumed too high, discount rates too low). Historical examples include the Dot-com Bubble (1995-2001), US Housing Bubble (2007-2009), and Crypto Boom-Busts (2017, 2021-2022).
*   **Real Options & Strategic Flexibility (Amazon):** Amazon's investment in AWS initially appeared to have a lower NPV than expanding its core retail operations, but it created a massive future growth platform and diversification.
*   **ESG & Regulatory Risk Mitigation (BP & Shell):** Energy firms face trade-offs where they may choose lower-NPV renewable energy projects over higher-NPV oil drilling to avoid massive regulatory risks, ESG risks, and commodity price volatility.
*   **Reputational Constraints (Nike):** Building a low-cost factory in a region with weak labor laws might yield a mathematically higher NPV, but management will often choose an ethically sourced facility to avoid stakeholder backlash and reputational damage.
*   **Central Bank Policy Divergence:** Bond yields and exchange rates are heavily impacted by central bank tone and policy divergences, as seen in the 1994 bond market sell-off and the post-pandemic recovery of 2022.

## 4. The Practitioner's Playbook
*   **Optimize Capital Rationing:** If capital is constrained, do not blindly choose the single highest-NPV project. **Select the combination of projects that generates the highest aggregate NPV within the budget limit**.
*   **Apply Risk-Adjusted Discount Rates (RADR):** **Never use the firm's standard WACC for all projects.** If a stable utility company evaluates a tech startup division, it must raise the discount rate to reflect the specific, higher risk of that project to avoid making terrible investments.
*   **Treat Credit Policy as an Investment:** When managing accounts receivable, weigh the revenue gained from lenient credit against contribution margins, bad debt costs, and financing costs. **Ask: "Are we buying revenue with working capital?"**
*   **Triangulate the Optimal Debt Level:** Do not rely on formulas alone to find optimal borrowing. **Combine quantitative WACC modeling, industry benchmarking (comparable firms), and target credit ratings** (e.g., borrowing only up to the level that sustains a 'BBB' rating).
*   **Stress-Test Liquidity:** Model what happens if sales drop 20%, customers delay payments by 15 days, or inventory turns slow by 10 days. **Calculate the immediate impact on the Cash Conversion Cycle (CCC) and line of credit usage**.

## 5. The Red Flags
*   **The Profit vs. Cash Disconnect:** **A firm can be highly profitable on an income statement but still go bankrupt** if it depletes its liquid cash pursuing rapid growth without collecting receivables. Cash is the engine of survival.
*   **Over-Leveraging / Financial Distress:** While debt lowers financing costs and provides a tax shield, **too much debt magnifies business risk**. It leads to credit downgrades, loss of customers, supplier restrictions, and bankruptcy.
*   **ESG-Washing:** **Markets only price ESG if the information is credible.** Unreliable disclosure causes valuation distortions, mispricing risks, and loss of investor trust.
*   **DDM Blind Spots:** The Dividend Discount Model is **highly sensitive to minor changes in growth or required return assumptions**, and is entirely useless for valuing growth firms that do not pay dividends.
*   **Agency Costs:** Watch for management teams making decisions to protect themselves rather than shareholders—such as **avoiding high-risk/high-reward projects to protect their jobs**, or wasting corporate capital on executive perks.
