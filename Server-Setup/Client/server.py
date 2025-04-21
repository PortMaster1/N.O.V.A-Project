import asyncio, requests

# REST API URL of your LLM server
IP = "192.168.12.138:8000"            # Update IP Address
CHAT_URL = f"http://{IP}/chat"
STATE_URL = f"http://{IP}/state"

async def get_response(text, model):
    response = await requests.post(CHAT_URL, json={"message": text})
    return response.json()["response"]

async def send_states(x, y, z, tilt):
    requests.post(STATE_URL, json={"states": [x, y, z, tilt]})
    return