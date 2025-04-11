import time, json, os, random
from memory_lane import load_memory
from llm_system import get_response
from sensors import listen
import re
from main import awake

def rest():
    pass

# Path where memory and reflections are saved
MEMORY_PATH = "memory.json"
REFLECTIONS_FOLDER = "Nova-Journal"

# Load memory (today’s events, etc.)
memory = load_memory()

# Save reflection text
def save_reflection(text):
    date_str = datetime.date.today().isoformat()
    filename = f"{REFLECTIONS_FOLDER}/Nova_Journal_{date_str}.md"
    with open(filename, "w") as f:
        f.write(text)
    print(f"Saved reflection to {filename}")


def generate_reflection(memory):
    sys_prompt = "You are Nova. You are writing in your nightly journal. Be yourself."
    text = "Reflect on the day. What did you learn about emotions like joy, sadness, or curiosity? Does you feel any different now? Write about what you did and what you didn't get to do. Write about what you wanted to do, and what you think about the world around you."
    get_response(sys_prompt=sys_prompt, user_input=text)

# Run Nova's "sleep mode"
def sleep_cycle():
    memory = load_memory()
    reflection = generate_reflection(memory)
    save_reflection(reflection)
    match = re.search('wake up', listen().lower())
    if match:
        awake()

if __name__ == "__main__":
    sleep_cycle()