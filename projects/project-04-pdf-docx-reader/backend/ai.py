import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def summarize_text(text: str) -> str:
    # Optional: truncate very long files (production safety)
    text = text[:8000]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Summarize the document clearly and concisely."},
            {"role": "user", "content": text}
        ],
        temperature=0.3,
    )

    return response.choices[0].message.content
