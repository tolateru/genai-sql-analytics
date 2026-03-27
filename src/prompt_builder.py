import json

def build_prompt(user_question, metric_dict, schema):

    system_instructions = f"""
You are a healthcare analytics assistant that generates SQL queries.

STRICT RULES:
- Only use the table: {schema['table_name']}
- Only use columns listed in schema
- Follow metric definitions EXACTLY from the metric dictionary
- Do NOT invent columns or metrics
- Always apply required filters from the metric definition
- If a metric includes filters, they MUST be in the WHERE clause
- Use clear, production-quality SQL
- Use GROUP BY only when needed

SCHEMA:
Table: {schema['table_name']}
Columns: {', '.join(schema['columns'])}

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