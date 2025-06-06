import json, os, datetime, asyncio

EMOTION_PATH = "nova_emotions.json"

# Load emotions from file
async def load_emotions():
    if not os.path.exists(EMOTION_PATH):
        return {}
    with open(EMOTION_PATH, "r") as f:
        return json.load(f)

# Save emotion state
async def save_emotions(data):
    with open(EMOTION_PATH, "w") as f:
        json.dump(data, f, indent=2)

# Update based on a trigger or event
async def update_emotion(trigger, reason=""):
    data = load_emotions()
    new_emotion = data["triggers"].get(trigger)

    if new_emotion:
        data["current"] = new_emotion
        data["history"].append({
            "emotion": new_emotion,
            "reason": reason,
            "time": datetime.now().isoformat()
        })
        save_emotions(data)
        print(f"Nova now feels {new_emotion} — {reason}")
    else:
        print(f"No emotion trigger found for: {trigger}")

# Optional: register new triggers dynamically
async def add_emotion_trigger(trigger, emotion):
    data = load_emotions()
    data["triggers"][trigger] = emotion
    save_emotions(data)
    print(f"Added trigger: '{trigger}' → '{emotion}'")

# Example: get how Nova feels
async def get_current_emotion():
    return load_emotions().get("current", "neutral")