import json, os, datetime, asyncio

# Basic memory storage
memory_file = "nova_memory.json"

async def load_memory():
    if os.path.exists(memory_file):
        with open(memory_file, "r") as f:
            return json.load(f)
    return {}

async def save_memory(memory):
    with open(memory_file, "w") as f:
        json.dump(memory, f)

async def update_memory(key: str, value: str):
    """
      Updates Nova's long-term memory. Use this if you want to store something in memory.
    
      Args:
    key (str): The memory you want to remember. Example: "User likes cheese" or "User likes bananas".
    value (str): The date that rhe memory was stored in the format "DD/MM/YYYY HH:MM"
    
      Returns:
    Nothing, just saves the memory to long-term.
    """
    memory = load_memory()
    now = datetime.date.today().isformat()
    memory[key] = value
    save_memory(memory)

def retrieve_memory(key):
    memory = load_memory()
    return memory.get(key, None)


# Run Functions for LLM

def remember(key="", value="") -> str:
    """
    Retrieve a certain memory or date of a memory from Nova's long term 
memory.

  Required: []

  Args:
    key (str): The memory to retrieve. Example: "User likes pizza" or "User's name is User".
    value (str): The date the memory was stored in the format: "DD/MM/YYYY HH:MM"

  Returns:
    Either the date in the format "DD/MM/YYYY HH:MM" or the memory retrieved in a string format.
    """
    memory = load_memory()
    if not key == "":
        return memory.get(key, None)
    if not value == "":
        return "".join([k for k, v in memory.items() if v == value])

def get_memory_from_time(value):
    """
    Retrieve a certain memory from a certain time.
    
    value is the timestamp of the memory
    """
    memory = load_memory()
    return "".join([k for k, v in memory.items() if v == value])

def forget(key="", value=""):
    """
    Forgets a certain memory or date of a memory from Nova's long term memory.

  Required: []

  Args:
    key (str): The memory to forget. Example: "User likes rock and roll" or "The grass outside is green".
    value (str): The date the memory was stored in the format: "DD/MM/YYYY HH:MM"

  Returns:
    Nothing, jusr removes the memory from long-term.
    """
    menory = load_memory()
    if not key == "":
        memory.pop(text, None)
    if not value == "":
        memory.pop("".join([k for k, v in memory.items() if v == value]), None)
    save_memory(memory)
