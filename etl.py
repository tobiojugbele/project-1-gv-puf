import os
import zipfile
import pandas as pd
import numpy as np

def run_puf_etl():
    print("🚀 Project 1 ETL: Ingesting and standardizing multi-file ZIP archive...")
    raw_dir = "data/raw"
    output_dir = "data/processed"
    os.makedirs(output_dir, exist_ok=True)

    zip_path = os.path.join(raw_dir, "2023_data_summary_spreadsheets.zip")
    if not os.path.exists(zip_path):
        print(f"❌ Target ZIP archive missing from: {zip_path}")
        return

    target_excel = "ghgp_data_2023.xlsx"
    print(f"📦 Extracting and parsing {target_excel} directly from ZIP...")

    try:
        with zipfile.ZipFile(zip_path, "r") as z:
            if target_excel not in z.namelist():
                print(f"❌ Could not locate {target_excel} inside the ZIP file archive.")
                print(f"Available files: {z.namelist()}")
                return
            with z.open(target_excel) as f:
                df = pd.read_excel(f, sheet_name=0, engine="openpyxl", low_memory=False)
    except Exception as e:
        print(f"❌ Ingestion pipeline failed: {str(e)}")
        return

    print(f"📋 Raw structural matrix shape ingested: {df.shape}")
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace("-", "_")

    fips_cols = [c for c in df.columns if "fips" in c]
    for col in fips_cols:
        df[col] = df[col].astype(str).str.split(".").str[0].str.zfill(5)
        print(f"✅ Formatted geography column string: {col}")

    value_cols = [c for c in df.columns if "spending" in c or "utilization" in c or "emissions" in c or "co2" in c]
    for col in value_cols:
        if df[col].dtype == "object":
            df[col] = df[col].astype(str).str.replace("$", "", regex=False).str.replace(",", "", regex=False)
            df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.replace(r"^\s*$", np.nan, regex=True)
    output_path = os.path.join(output_dir, "cleaned_gv_puf.csv")
    df.to_csv(output_path, index=False)
    print(f"🎉 Processed pipeline completed. Standardized data stored at: {output_path}")

if __name__ == "__main__":
    run_puf_etl()
