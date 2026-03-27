import duckdb
import pandas as pd
import os

def run_sql_on_csv(sql: str, csv_path: str) -> pd.DataFrame:
    con = duckdb.connect()

    # Register the CSV as the table your SQL expects
    con.execute(f"""
        CREATE OR REPLACE VIEW healthcare_claims AS
        SELECT * FROM read_csv_auto('{csv_path}', HEADER=TRUE);
    """)

    df = con.execute(sql).df()
    con.close()
    return df