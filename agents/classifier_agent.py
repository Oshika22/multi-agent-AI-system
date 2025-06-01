# agents/classifier_agent.py
from utils.llm_utils import detect_format_and_intent
import json

def classify_input(input_text):
    raw_response = detect_format_and_intent(input_text)
    return raw_response
