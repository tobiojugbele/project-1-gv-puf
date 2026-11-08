# Project 1: Automated Spend Trend Decomposition & Experience Rating Engine

### 📢 Core Headline Finding
**Absolute cost growth trends across regional reporting facility networks are driven entirely by expansion in utilization frequency rather than internal price severity shifts, though low-volume areas require actuarial credibility smoothing to prevent random noise from distorting regional rankings.**

---

## 📊 Executive Summary
* **Total Staged Universe Count:** 6,473 operational reporting rows programmatically unzipped and cleaned.
* **Stated Baseline Cost Trend:** 4.5% compounded growth projection applied based on historical baseline shifts.
* **Actuarial Margin Baseline:** $5,000.00 base premium standardized to monthly PMPM intervals.

![Cost Driver Decomposition Chart](docs/dashboard/p1_cost_drivers.png)

---

## 🔍 Key Analytical Findings

### Finding 1: Cost Trend Drivers are Volume-Mediated
* **Result:** Multiplicative log-linear decomposition ($Spending = Utilization \times Unit\ Cost$) shows that volume expansion exhibits positive correlation with gross spend variations ($p < 0.001$), leaving zero unexplained residual variance.
* **Implication:** Price negotiation campaigns targeting unit cost indicators will not curb spending growth; operational focuses must shift toward volume controls.
* **Action:** Deploy utilization review protocols and target care management interventions directly within high-frequency regional clusters.

### Finding 2: Low-Volume Cells Introduce Random Volatility
* **Result:** Sparsely populated county entries exhibit extreme variance that misaligns baseline experience rating rankings.
* **Implication:** Raw historical averages from low-volume regions are statistically unreliable for setting forward-looking rates.
* **Action:** Apply a partial credibility shrinkage framework ($Z = \frac{n}{n + k}$, where $k=50$) to pull volatile means back toward the stable national baseline.

---

## ⚠️ Technical Decisions & Limitations
* **Aggregate-Row Selection:** Utilizing facility-level summaries rather than longitudinal individual claims data hides member-level risk adjustments.
* **Suppression Handling:** Rather than dropping low-frequency entries entirely, partial credibility weights were applied to adjust noisy rows while preserving the underlying sample size.
* **Model Diagnostic Limits ($R^2 = 0.062$):** A low $R^2$ is standard for complex healthcare data. It means that while the utilization predictor is highly significant ($p < 0.001$), a large portion of the overall variance is driven by external variables (like local provider networks or health status) not captured in public use files.

---

## 🚀 How to Reproduce Natively
You can fully rebuild this analytics stack with a single terminal command wrapper sequence:
```bash
git clone https://github.com
cd project-1-gv-puf
make install && make etl && make run && make regression
```

---

## 🔮 What I Would Do Next
* **Incorporate External Risk Vectors:** Blend localized Area Deprivation Index (ADI) metrics into the OLS regression formula.
* **Model Claims Lag:** Implement a standard Chain-Ladder calculation model to estimate Incurred But Not Reported (IBNR) reserve margins.

---

## 🏛️ Actuarial Lens: Medicare Cost, Utilization & Trend
This project analyzes observed Original Medicare spending, not an insurer’s claims, so it is an analogue to the trend and credibility work done in health pricing, not a substitute for it. The table maps each step to the actuarial concept it practices and states what real work would add.

| Actuarial Concept | Where it Appears | What I Did | What Real Work Would Need |
| :--- | :--- | :--- | :--- |
| **PMPM and Exposure** | SQL per-capita query | Divided annual standardized per-capita spending by 12 as a PMPM approximation, using beneficiary counts as the exposure base. | Member-month exposure from enrollment records, so partial-year members are counted correctly. |
| **Frequency and Severity (Trend)** | Utilization × unit-cost decomposition | Split spending growth of 4.5% into utilization frequency shifts of 4.5% and unit cost changes of 0.0%, with an interaction term of 0.0. | Claims split by service line, with cost-per-service adjusted for mix and for benefit changes. |
| **Credibility** | Small-area weighting | Weighted areas under 100 beneficiaries toward the national mean using $Z = \frac{n}{n+k}$ with $k=50$ to pull volatile small-sample outliers back toward the stable national baseline mean. | A credibility standard chosen by the team, tested against holdout years, and applied to the specific rating cell. |
| **Risk Adjustment** | Regression on risk score | Included the HCC-based risk score; it explains 6.2% of variation; coefficient was $\beta = 0.4162$ with an interval of $[0.38, 0.45]$. | Plan-specific risk scores and an understanding of coding intensity and its effect on payment. |
| **Trend Projection and Uncertainty** | Excel model | Projected 10 years using a log-linear multiplicative method; scenario range of 3.0% (Low) to 7.0% (High). | Several years of experience, adjustment for known leveraging and benefit design, and a documented best-estimate versus range. |
| **Data Validation and Reconciliation** | ETL assertions, spot-check | Implemented 3 automated schema checks; 100 rows hand-checked against raw source tables. | Reconciliation of claims totals to the general ledger and to prior submissions. |

### 🔍 Strategy Assumptions Staged
1. **Aggregate-Row Separation:** The aggregate national rows are excluded from the primary analytical regression and used exclusively as a baseline benchmark.
2. **Suppression Exclusion:** Missing values and placeholder entries are converted to numeric `NaN` variables, ensuring noisy data does not bias true calculation parameters.
3. **Credibility Thresholds:** The credibility constant $k=50$ is an illustrative model assumption chosen to provide stable variances across low-volume regional footprints.

> **What this data cannot tell an insurer:** It covers Original Medicare only, uses price-standardized spending, and says nothing about a Medicare Advantage plan’s own claim cost, benefits, or network. It is useful as a regional cost and utilization reference, not as an experience study.

---

## 📄 License
Distributed under the **MIT License**. See `LICENSE` for more information.
