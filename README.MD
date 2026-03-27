# GenAI Analytics Copilot

A Streamlit-based healthcare analytics assistant that converts natural language into governed SQL and executes it against a healthcare claims dataset.

## Features
- Natural language to SQL
- Metric dictionary governance
- Schema-aware prompting
- SQL execution with DuckDB
- Streamlit UI

## Run locally
```bash
pip install -r requirements.txt
python -m streamlit run src/ui.py