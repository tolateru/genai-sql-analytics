import streamlit as st
import json
import os
from dotenv import load_dotenv
from prompt_builder import build_prompt
from sql_generator import generate_sql
from query_runner import run_sql_on_csv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

claims_csv_path = os.path.join(BASE_DIR, "data", "healthcare_claims_100k.csv")
provider_csv_path = os.path.join(BASE_DIR, "data", "provider_reference.csv")

with open(os.path.join(BASE_DIR, "config", "metric_dictionary.json"), "r") as f:
    metric_dict = json.load(f)

with open(os.path.join(BASE_DIR, "config", "schema.json"), "r") as f:
    schema = json.load(f)

st.set_page_config(page_title="Healthcare GenAI SQL Assistant", layout="wide")

# Sidebar - Semantic Layer
st.sidebar.title("Analytics Guide")

st.sidebar.header("Available Metrics")
metrics = [
    "Total Paid Amount",
    "Total Drug Spend",
    "Denied Claims Count",
    "Pending Claims Count",
    "Reversal Rate",
    "Average Cost Per Claim"
]
for metric in metrics:
    st.sidebar.write(f"- {metric}")

st.sidebar.header("Available Dimensions")
dimensions = [
    "Provider Specialty",
    "Claim Type",
    "Member State",
    "Place of Service",
    "Service Date",
    "Drug Code",
    "Provider Region",
    "Provider Network Status",
    "Provider Contract Type",
    "Provider Group"
]
for dimension in dimensions:
    st.sidebar.write(f"- {dimension}")

st.sidebar.header("Available Tables")
tables = ["healthcare_claims", "provider_reference"]
for table in tables:
    st.sidebar.write(f"- {table}")

st.sidebar.header("Sample Questions")
examples = [
    "Show total paid amount by provider region",
    "Compare denied claims by provider network status",
    "Show reversal rate by provider group",
    "Show drug spend by provider contract type",
    "Show average paid amount by claim type"
]

for example in examples:
    if st.sidebar.button(example):
        st.session_state["question"] = example

st.title("Healthcare GenAI SQL Assistant")

question = st.text_input(
    "Ask a healthcare analytics question:",
    value=st.session_state.get("question", "")
)

if st.button("Generate SQL") and question:
    try:
        prompt = build_prompt(question, metric_dict, schema)
        sql = generate_sql(prompt)

        st.subheader("Generated SQL")
        st.code(sql, language="sql")

        st.subheader("Query Results")
        results_df = run_sql_on_csv(sql, claims_csv_path, provider_csv_path)
        st.dataframe(results_df, use_container_width=True)

        st.caption(f"Returned {len(results_df)} rows")

    except Exception as e:
        st.error(f"Error: {str(e)}")
