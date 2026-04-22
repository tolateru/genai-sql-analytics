import json

def build_prompt(user_question, metric_dict, schema):
    tables_text = []
    for table_name, table_info in schema["tables"].items():
        table_description = table_info.get("description", "")
        columns = table_info.get("columns", [])
        tables_text.append(
            f"Table: {table_name}\n"
            f"Description: {table_description}\n"
            f"Columns: {', '.join(columns)}"
        )

    joins_text = []
    for join in schema.get("joins", []):
        joins_text.append(
            f"{join['join_type']} JOIN {join['left_table']}.{join['left_column']} = "
            f"{join['right_table']}.{join['right_column']} "
            f"({join.get('description', '')})"
        )

    system_instructions = f"""
You are a healthcare analytics assistant that generates SQL queries.

STRICT RULES:
- Only use the tables listed in the schema
- Only use columns listed for each table
- Follow metric definitions EXACTLY from the metric dictionary
- Do NOT invent columns, tables, metrics, or joins
- Only use join relationships explicitly listed in the schema
- If a metric includes filters, they MUST be applied in the WHERE clause
- Use clear, production-quality SQL
- Use table aliases when joins are involved
- Return ONLY raw SQL
- Do not use markdown
- Do not wrap the answer in ```sql or ```
- No explanations

AVAILABLE TABLES:
{chr(10).join(tables_text)}

VALID JOINS:
{chr(10).join(joins_text)}

METRIC DEFINITIONS:
{json.dumps(metric_dict, indent=2)}

OUTPUT FORMAT:
- Return ONLY raw SQL
- Do not use markdown
- Do not wrap the answer in ```sql or ```
- No explanations
"""

    final_prompt = f"""
{system_instructions}

USER QUESTION:
{user_question}
"""

    return final_prompt
