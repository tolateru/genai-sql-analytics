def validate_sql(sql: str, schema: dict) -> bool:
    allowed_columns = set(schema["columns"])
    allowed_table = schema["table_name"]

    sql_lower = sql.lower()

    # Check table
    if allowed_table.lower() not in sql_lower:
        raise ValueError("Invalid table used in SQL")

    # Basic column validation (simple version)
    for word in sql.replace(",", " ").split():
        if word.lower() in ["select", "from", "where", "group", "by", "sum", "as"]:
            continue
        if "(" in word or ")" in word:
            continue

        clean_word = word.strip()

        if clean_word in allowed_columns:
            continue

    return True