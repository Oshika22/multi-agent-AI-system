
import requests
import json
import sqlite3
from datetime import datetime
API_KEY = "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"
API_URL = "https://openrouter.ai/api/v1/chat/completions"
# Function to pass the prompt to LLM
def call_openrouter(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "mistralai/devstral-small:free",  # Or another free model like "gemma:7b"
        "messages": [
            {"role": "system", "content": "You are a helpful classifier."},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(API_URL, headers=headers, json=data)

    try:
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        print("Error decoding JSON:", e)
        return None

# LLM functionto classify the file type
import re
import json
def detect_format_and_intent(input_text):
    prompt = f"""
You are a smart AI agent.

Analyze the following input and determine:
- What format is it? (Email, JSON, PDF text, Plain Text, etc.)
- What is the user's intent?

Return *only* valid JSON like:
{{ "format": "Email", "intent": "Complaint" }}

Input:
---
{input_text}
---
"""
    response = call_openrouter(prompt)

    if response is None:
        return {"format": "Unknown", "intent": "Unknown"}

    # Try to extract JSON from messy LLM response
    try:
        # This regex finds the JSON object inside any text
        match = re.search(r"\{.*\}", response, re.DOTALL)
        if match:
            return json.loads(match.group(0))
        else:
            print("No JSON found in response.")
            return {"format": "Unknown", "intent": "Unknown"}
    except json.JSONDecodeError as e:
        print("LLM returned invalid JSON:", e)
        print("Raw response:", response)
        return {"format": "Unknown", "intent": "Unknown"}
