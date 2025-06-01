from agents.classifier_agent import classify_input
from agents.json_agent import process_json_input
from agents.email_agent import process_email
from memory.memory_store import log_to_memory
from memory.memory_store import get_memory_logs
import json
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def run_flow(input_data):
    classification = classify_input(input_data)
    print("\n[Classifier Output]", classification)
    input_type = classification['format'].lower()
    log_to_memory(source="User", type=input_type, intent=classification['intent'], extracted={})
    
    if input_type == "json":
        result = process_json_input(input_data)
    elif input_type == "email":
        result = process_email(input_data)
    else:
        print("Unsupported input type.")
        return

    log_to_memory(source="User", type=input_type, intent=classification['intent'], extracted=result)
    print("\n[Final Extracted Result]", result)


if __name__ == "__main__":
    # Choose input to simulate
    with open("sample_inputs/sample_email.txt", "r") as f:
        email_data = f.read()

    with open("sample_inputs/sample_json.json", "r") as f:
        json_data = json.load(f)

    print("\n=== Simulating Email Input ===")
    run_flow(email_data)

    print("\n=== Simulating JSON Input ===")
    run_flow(json_data)
    print("\n=== 📚 Memory Logs ===")
    logs = get_memory_logs()
    for log in logs:
        print(f"[{log['timestamp']}] {log['type']} | {log['intent']} | {log['extracted']}")
