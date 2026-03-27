import os
from openai import OpenAI

def generate_sql(prompt: str) -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found. Check your .env file.")

    client = OpenAI(api_key=api_key)

    response = client.responses.create(
        model="gpt-4.1",
        input=prompt
    )

    return response.output_text.strip()