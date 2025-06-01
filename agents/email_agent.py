# agents/email_agent.py
from utils.llm_utils import call_openrouter
import json

def process_email(email_text):
    prompt = f"""
You are an intelligent assistant. Extract the following fields from the email content below:
- Sender (if mentioned)
- Intent of the email
- Urgency (High / Medium / Low)

Respond ONLY in JSON format like:
{{
  "sender": "...",
  "intent": "...",
  "urgency": "High"
}}

Email:
\"\"\"
{email_text}
\"\"\"
"""
    raw_response = call_openrouter(prompt)
    
    try:
        return json.loads(raw_response)
    except Exception as e:
        print("LLM failed to parse email correctly:", e)
        print("Raw response:", raw_response)
        return {
            "sender": "Unknown",
            "intent": "Unknown",
            "urgency": "Unknown"
        }
