import os
import sqlite3
import pandas as pd
import pytest

def test_processed_data_integrity():
    csv_path = "data/processed/cleaned_gv_puf.csv"
    assert os.path.exists(csv_path), "❌ Processed flat file output missing!"
    df = pd.read_csv(csv_path)
    
    assert df['state'].notnull().all(), "❌ Null states found!"
    assert df['reporting_year'].between(2000, 2026).all(), "❌ Reporting timeline scope breach!"

def test_database_persistence():
    db_path = "data/gv_puf.db"
    assert os.path.exists(db_path), "❌ SQLite database file not staged!"
    
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query("SELECT * FROM facilities LIMIT 5;", conn)
    conn.close()
    assert not df.empty, "❌ Database table 'facilities' is empty!"
