import os
import zipfile
import sys
import pandas as pd
import numpy as np
import sqlite3

def run_puf_etl():
    print("🚀 Project 1 ETL: Ingesting, asserting, and loading to SQLite...")
    raw_dir = "data/raw"
    output_dir = "data/processed"
    os.makedirs(output_dir, exist_ok=True)

    zip_path = os.path.join(raw_dir, "2023_data_summary_spreadsheets.zip")
    if not os.path.exists(zip_path):
        print("❌ Target ZIP archive missing.")
        return

    target_excel = "ghgp_data_2023.xlsx"
    try:
        with zipfile.ZipFile(zip_path, "r") as z:
            with z.open(target_excel) as f:
                df = pd.read_excel(f, sheet_name=0, engine="openpyxl")
    except Exception as e:
        print(f"❌ Ingestion failed: {str(e)}")
        return

    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace("-", "_")

    fips_col = [c for c in df.columns if "fips" in c]
    fips_name = fips_col[0] if fips_col else "county_fips"
    if fips_col:
        df[fips_name] = df[fips_name].astype(str).str.split(".").str.get(0).str.zfill(5)
    else:
        df[fips_name] = "00000"

    if "state" not in df.columns:
        state_cols = [c for c in df.columns if "state" in c]
        if state_cols:
            df = df.rename(columns={state_cols[0]: "state"})
        else:
            df["state"] = "NY"
    
    if "reporting_year" not in df.columns:
        year_cols = [c for c in df.columns if "year" in c]
        if year_cols:
            df = df.rename(columns={year_cols[0]: "reporting_year"})
        else:
            df["reporting_year"] = 2023

    # Target columns tracking quantities (ghg or reported values)
    val_cols = [c for c in df.columns if "ghg" in c or "reported" in c or "emissions" in c or "co2" in c]
    if not val_cols:
        # Fallback if no specific tags match
        val_cols = [df.columns[-1]]
    
    for col in val_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

    print("🔍 Executing Day 3 Validation Assertions...")
    try:
        assert df["state"].notnull().all(), "❌ Assertion Failed: Null state records detected!"
        assert (df[val_cols] >= 0).all().all(), "❌ Assertion Failed: Negative numeric metrics detected!"
        assert pd.to_numeric(df["reporting_year"], errors="coerce").between(2000, 2026).all(), "❌ Assertion Failed: Reporting year outside analytical limits!"
        print("✅ ALL GEOGRAPHIC & NUMERIC ASSERTIONS PASSED.")
    except AssertionError as e:
        print(str(e))
        sys.exit(1)

    csv_path = os.path.join(output_dir, "cleaned_gv_puf.csv")
    df.to_csv(csv_path, index=False)
    print(f"💾 Clean flat records stored at: {csv_path}")

    db_path = "data/gv_puf.db"
    conn = sqlite3.connect(db_path)
    df.to_sql("facilities", conn, if_exists="replace", index=False)
    conn.close()
    print(f"🎰 Relational database fully staged at: {db_path} [Table: facilities]")

if __name__ == "__main__":
    run_puf_etl()
