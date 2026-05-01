import json
import os

MEMORY_FILE = "memory/memory.json"

def save_input(user_input):
    data = []

    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            data = json.load(f)

    data.append({"input": user_input})

    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=2)

    return data
