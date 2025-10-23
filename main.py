import json

def process_data(input_path: str) -> str:
    """
    Example processing function.
    Reads JSON, performs dummy transformation, and returns stringified result.
    """
    with open(input_path, "r") as f:
        data = json.load(f)
    print("Data loaded successfully.")
    # Dummy logic for demo
    processed = {"count": len(data), "status": "processed"}

    return json.dumps(processed, indent=4)
