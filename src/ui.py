import streamlit as st
import json
import os
from dotenv import load_dotenv
from prompt_builder import build_prompt
from sql_generator import generate_sql
from query_runner import run_sql_on_csv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
csv_path = os.path.join(BASE_DIR, "data", "healthcare_claims_100k.csv")

with open(os.path.join(BASE_DIR, "config", "metric_dictionary.json"), "r") as f:
    metric_dict = json.load(f)

with open(os.path.join(BASE_DIR, "config", "schema.json"), "r") as f:
    schema = json.load(f)

st.set_page_config(page_title="Healthcare GenAI SQL Assistant", layout="wide")
st.title("Healthcare GenAI SQL Assistant")

question = st.text_input("Ask a healthcare analytics question:")

if st.button("Generate SQL") and question:
    try:
        prompt = build_prompt(question, metric_dict, schema)
        sql = generate_sql(prompt)

        st.subheader("Generated SQL")
        st.code(sql, language="sql")

        st.subheader("Query Results")
        results_df = run_sql_on_csv(sql, csv_path)
        st.dataframe(results_df, use_container_width=True)

        st.caption(f"Returned {len(results_df)} rows")

    except Exception as e:
        st.error(f"Error: {str(e)}")