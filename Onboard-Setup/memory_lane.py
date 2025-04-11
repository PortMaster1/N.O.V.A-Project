import json, os
from datetime import datetime

# Basic memory storage
memory_file = "nova_memory.json"

def load_memory():
    if os.path.exists(memory_file):
        with open(memory_file, "r") as f:
            return json.load(f)
    return {}

def save_memory(memory):
    with open(memory_file, "w") as f:
        json.dump(memory, f)

def update_memory(key, value):
    memory = load_memory()
    memory[key] = value
    save_memory(memory)

def retrieve_memory(key):
    memory = load_memory()
    return memory.get(key, None)


# Run Functions for LLM

def remember(text):
    now = datetime.date.today().isoformat(
    update_memory(text, now)

def forget(text):
    menory = load_memory()
    memory.pop(text, None)
    save_memory(memory)