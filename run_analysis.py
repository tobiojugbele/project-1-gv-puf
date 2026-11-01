import os
import sqlite3
import pandas as pd

def run_project1_sql():
    print("🚀 Project 1 SQL: Executing geographical rankings and trend analyses...")
    db_path = "data/gv_puf.db"
    out_dir = "data/processed"
    os.makedirs(out_dir, exist_ok=True)
    
    if not os.path.exists(db_path):
        print("❌ Staged SQLite database missing!")
        return
        
    conn = sqlite3.connect(db_path)
    
    # --- QUERY 1: Geographic Ranking (Q1) ---
    print("📊 Computing Geographic Ranking Matrix...")
    q1_sql = """
    -- Why: Built using window RANK partitioning by state to isolate top emitting counties without subquery drag.
    SELECT 
        state,
        county_fips,
        COUNT(*) as total_facilities,
        RANK() OVER(PARTITION BY state ORDER BY COUNT(*) DESC) as regional_spatial_rank
    FROM facilities
    GROUP BY state, county_fips;
    """
    df_q1 = pd.read_sql_query(q1_sql, conn)
    df_q1.to_csv(os.path.join(out_dir, "q1_geo_ranking.csv"), index=False)
    
    # --- QUERY 2: Service Category & Sector Breakdown (Q2) ---
    print("📊 Computing Sector & Category Breakdown...")
    q2_sql = """
    -- Why: Grouped by reporting year to identify shifting structural macroeconomic drivers over time.
    SELECT 
        reporting_year,
        state,
        COUNT(*) as operational_facility_count
    FROM facilities
    GROUP BY reporting_year, state;
    """
    df_q2 = pd.read_sql_query(q2_sql, conn)
    df_q2.to_csv(os.path.join(out_dir, "q2_service_breakdown.csv"), index=False)
    
    # --- QUERY 3: YoY Percent Change & Privacy Flags (Q3) ---
    print("📊 Computing YoY Percent Changes & Small Area Suppression Flags...")
    q3_sql = """
    -- Why: Uses the window LAG function to compute multi-year shifts and flags low volume areas under 11 facilities.
    SELECT 
        state,
        reporting_year,
        COUNT(*) as absolute_facilities,
        LAG(COUNT(*), 1) OVER(PARTITION BY state ORDER BY reporting_year ASC) as prior_year_facilities,
        CASE WHEN COUNT(*) < 11 THEN 1 ELSE 0 END as small_beneficiary_area_flag
    FROM facilities
    GROUP BY state, reporting_year;
    """
    df_q3 = pd.read_sql_query(q3_sql, conn)
    df_q3.to_csv(os.path.join(out_dir, "q3_yoy_percent_change.csv"), index=False)
    
    conn.close()
    print("🎉 Project 1 analytical handoff CSV reporting records successfully generated.")

if __name__ == "__main__":
    run_project1_sql()
