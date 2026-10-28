import os
import pandas as pd
import numpy as np

def run_puf_etl():
    print("🚀 Project 1 ETL: Ingesting and standardizing GV PUF dataset...")
    raw_dir = "data/raw"
    if not os.path.exists(raw_dir):
        print("❌ Data directory missing.")
        return
    raw_files = [os.path.join(raw_dir, f) for f in os.listdir(raw_dir) if f.endswith(".csv") or f.endswith(".zip")]
    if not raw_files:
        print("❌ No raw CSV or ZIP file discovered in data/raw/")
        return
    df = pd.read_csv(raw_files[0], low_memory=False)
    print(f"📋 Raw structural shape ingested: {df.shape}")
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace("-", "_")
    fips_cols = [c for c in df.columns if "fips" in c]
    for col in fips_cols:
        df[col] = df[col].astype(str).str.split(".").str[0].str.zfill(5)
        print(f"✅ Formatted geography column: {col}")
    value_cols = [c for c in df.columns if "spending" in c or "utilization" in c or "emissions" in c]
    for col in value_cols:
        if df[col].dtype == "object":
            df[col] = df[col].astype(str).str.replace("$", "", regex=False).str.replace(",", "", regex=False)
            df[col] = pd.to_numeric(df[col], errors="coerce")
    df = df.replace(r"^\s*$", np.nan, regex=True)
    os.makedirs("data/processed", exist_ok=True)
    output_path = "data/processed/cleaned_gv_puf.csv"
    df.to_csv(output_path, index=False)
    print(f"🎉 Processed pipeline completed. Standardized data stored at: {output_path}")

if __name__ == "__main__":
    run_puf_etl()
