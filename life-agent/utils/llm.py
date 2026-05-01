import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("API_KEY"),
    base_url=os.getenv("BASE_URL")
)

def call_llm(prompt):
    response = client.chat.completions.create(
        model="mimo-v2.5",
        messages=[
            {"role": "system", "content": "你是一个专业的行为分析AI"},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content
