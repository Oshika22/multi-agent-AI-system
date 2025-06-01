# agents/json_agent.py
def validate_json_against_schema(input_data, schema):
    issues = []

    for key, expected_type in schema.items():
        if key not in input_data:
            issues.append(f"Missing field: {key}")
        elif not isinstance(input_data[key], expected_type):
            issues.append(f"Incorrect type for {key}: expected {expected_type.__name__}, got {type(input_data[key]).__name__}")

    return issues


def process_json_input(input_data):
# Chicking the targeted schema
    from memory.target_schema import TARGET_SCHEMA  

    issues = validate_json_against_schema(input_data, TARGET_SCHEMA)
# Formating the input
    formatted_output = {
        "name": input_data.get("name", "N/A"),
        "email": input_data.get("email", "N/A"),
        "age": input_data.get("age", "N/A"),
        "request_type": input_data.get("request_type", "N/A"),
        "details": input_data.get("details", "N/A")
    }

    return {
        "formatted": formatted_output,
        "anomalies": issues
    }

