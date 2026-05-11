from openai import OpenAI
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

df = pd.read_csv("sample_bom.csv")

bom_text = df.to_string(index=False)

prompt = f"""
You are an enterprise storage and CPQ validation assistant.

Analyze this BOM and identify:
- compatibility risks
- missing licenses
- deployment concerns
- upsell opportunities

BOM:
{bom_text}
"""

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

print(response.choices[0].message.content)