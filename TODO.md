# Next Session Tasks: Day 4 Launchpad (Project 1)

## 🗄️ 1. Environment Verification
- [ ] Open the terminal and verify the environment matches the local repository state.
- [ ] Run `make test` to ensure directory paths and virtual environment wrappers (`(venv)`) are active and stable.

## 🔌 2. Establish Power BI Data Connections
- [ ] Launch your Windows virtualization environment (Parallels, VMware, or standalone PC).
- [ ] Open **Power BI Desktop**.
- [ ] Select **Get Data > More... > Database > SQLite Database** (or select the SQLite ODBC Driver link).
- [ ] Route the filepath pointer directly to your processed relational tracking file: `~/project-1-gv-puf/data/gv_puf.db`.
- [ ] Select the `facilities` table from the Navigator menu matrix and click **Load**.

## 📐 3. Construct Core Analytical DAX Measures
Build explicit calculations to isolate metrics and solve business questions **Q1, Q2, and Q3** directly from the SQLite staging records without causing duplication or aggregate distortion:
- [ ] **Total Verified Emissions:** Write a measure to compute the baseline sum of greenhouse gas emissions (`SUM(facilities[reported_emissions])`).
- [ ] **Active Reporting Units Count:** Create a measure to evaluate the distribution footprint of unique facilities (`DISTINCTCOUNT(facilities[facility_id])`).
- [ ] **Missing Value Audit Ratio (Q3 Metric):** Script a calculation to identify the volume and percentage of blank rows or `NaN` attributes across non-required fields.

## 📊 4. Design Dashboard Layout Wireframe
- [ ] Initialize a clean visual layout framework utilizing card elements to surface high-level summary totals.
- [ ] Group facility reporting segments by industry type, parent company ownership networks, and regional state jurisdictions.
