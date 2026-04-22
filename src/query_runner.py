import duckdb
import pandas as pd
import os

def run_sql_on_csv(sql: str, claims_csv_path: str, provider_csv_path: str) -> pd.DataFrame:
    con = duckdb.connect()

    claims_csv_path = claims_csv_path.replace("\\", "/")
    provider_csv_path = provider_csv_path.replace("\\", "/")

    con.execute(f"""
        CREATE OR REPLACE VIEW healthcare_claims AS
        SELECT * FROM read_csv_auto('{claims_csv_path}', HEADER=TRUE);
    """)

    con.execute(f"""
        CREATE OR REPLACE VIEW provider_reference AS
        SELECT * FROM read_csv_auto('{provider_csv_path}', HEADER=TRUE);
    """)

    df = con.execute(sql).df()
    con.close()

    return df
