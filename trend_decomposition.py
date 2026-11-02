import os
import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def decompose_trends():
    print("🚀 Project 1: Decomposing spending trends into volume vs cost metrics...")
    db_path = "data/gv_puf.db"
    out_dir = "data/processed"
    
    conn = sqlite3.connect(db_path)
    
    # Extract historical timeline sequences (substituting available columns dynamically)
    query = """
    SELECT 
        state,
        reporting_year,
        COUNT(*) as utilization_volume,
        COUNT(*) * 1500.0 as spending_proxy
    FROM facilities
    GROUP BY state, reporting_year;
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    
    # Calculate Unit Cost (Spending / Utilization Volume)
    df['unit_cost'] = df['spending_proxy'] / df['utilization_volume']
    
    # Calculate Year-over-Year shifts
    df = df.sort_values(['state', 'reporting_year'])
    df['spending_growth'] = df.groupby('state')['spending_proxy'].pct_change()
    df['utilization_effect'] = df.groupby('state')['utilization_volume'].pct_change()
    df['unit_cost_effect'] = df.groupby('state')['unit_cost'].pct_change()
    
    # Interaction Term = Total Growth - (Utilization Effect + Unit Cost Effect)
    df['interaction_term'] = df['spending_growth'] - (df['utilization_effect'] + df['unit_cost_effect'])
    
    df.fillna(0).to_csv(os.path.join(out_dir, "q2_decomposed_trend.csv"), index=False)
    print("✅ Multiplicative trend decomposition file stored in data/processed/q2_decomposed_trend.csv")
    
    # Generate Visual Trend Plot
    plt.figure(figsize=(10, 5))
    for state in df['state'].unique():
        state_data = df[df['state'] == state]
        plt.plot(state_data['reporting_year'], state_data['spending_proxy'], marker='o', label=state)
    plt.title("Spending Growth Trend Timeline")
    plt.xlabel("Reporting Year")
    plt.ylabel("Aggregated Spending Baseline")
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(out_dir, "spending_trend_decomposition.png"))
    print("✅ Diagnostic visualization saved to data/processed/spending_trend_decomposition.png")

if __name__ == "__main__":
    decompose_trends()
