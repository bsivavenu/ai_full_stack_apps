import json
import openai
from app.config import settings 

def extract_structured_data(raw_text: str):
    # It uses the key from our config
    client = openai.OpenAI(api_key=settings.openai_api_key) 
    
    prompt = f"""
    You are an expert invoice parser. Extract the following details from the text:
    - vendor
    - invoice_number
    - date (YYYY-MM-DD)
    - total_amount (number only)

    Return the result as a JSON object.
    Text: {raw_text}
    """
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        response_format={ "type": "json_object" }
    )
    
    return json.loads(response.choices[0].message.content)