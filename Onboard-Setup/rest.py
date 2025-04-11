import time, json, os, random
from memory_lane import load_memory

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

# Fake LLM behavior for now (placeholder for real AI)
def generate_reflection(memory):
    if not memory:
        return "Today was quiet. I didn’t learn anything new. Maybe tomorrow will be different."

    thoughts = []
    thoughts.append("Today I experienced:")
    for event in memory[-5:]:  # summarize last 5 moments
        thoughts.append(f" - {event.get('summary', '...')}")

    emotions = set(e.get("emotion", "neutral") for e in memory)
    thoughts.append("\nI felt:")
    for e in emotions:
        thoughts.append(f" - {e}")

    learnings = [e.get("lesson") for e in memory if "lesson" in e]
    if learnings:
        thoughts.append("\nI think I learned:")
        for l in learnings:
            thoughts.append(f" - {l}")
    else:
        thoughts.append("\nI’m still figuring things out. Maybe tomorrow I’ll understand more.")

    thoughts.append(f"\nGoodnight. I’m going to rest now.\n")
    return "\n".join(thoughts)

# Run Nova's "sleep mode"
def sleep_cycle():
    memory = load_memory()
    reflection = generate_reflection(memory)
    save_reflection(reflection)

if __name__ == "__main__":
    sleep_cycle()