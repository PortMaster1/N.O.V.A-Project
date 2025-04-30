import time, json, os, random, re
from . import load_memory
from . import llm_system
from . import sensors

load_memory = memory_lane.load_memory
get_response = llm_system.get_response
listen = sensors.listen

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
    text = "Reflect on the day. What did you learn about emotions like joy, sadness, or curiosity? Does you feel any different now? Write about what you did and what you didn't get to do. Write about what you wanted to do, and what you think about the world around you."
    get_response(text, "nightmodel")

# Run Nova's "sleep mode"
def sleep_cycle():
    memory = load_memory()
    if not os.path.exists(f"{REFLECTIONS_FOLDER}/Nova_Journal_{date_str}.md"):
        reflection = generate_reflection(memory)
        save_reflection(reflection)
    while True:
        match = re.search('wake up', listen().lower())
        if match:
            return "awake"
            break
        time.sleep(5)
        primt("Sleeping..."

if __name__ == "__main__":
    sleep_cycle()
