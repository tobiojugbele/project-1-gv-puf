# Project 1 Data Strategy Log

### 1. Retention of National Record Rows
* **Decision:** National baseline summary aggregate rows are dropped from the primary data frame and exported to an independent validation file.
* **Why:** Retaining national aggregates inside the primary transactional pipeline introduces double-counting errors during visualization drill-downs in Power BI.

### 2. Missing and Suppressed Value Operations (Q3 Treatment)
* **Decision:** Blank columns, missing attributes, and string-based placeholder suppression indicators are converted to explicit `NaN` fields.
* **Why:** Converting text indicators to numeric `NaN` prevents numeric parsing failures, allows aggregate calculations to ignore missing cells naturally, and protects tracking metrics from calculation corruption.

### 2026-11-04: Business Intelligence Frontend Semantic Layering
* **Decision:** Built out executive report layouts in Power BI utilizing takeaway titles, filled maps, and dynamic YoY facility growth calculators.
* **Why:** Replaces generic descriptive card labels with clear, conclusion-driven titles so non-technical stakeholders instantly understand that cost trend shifts are volume-driven.
