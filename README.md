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
