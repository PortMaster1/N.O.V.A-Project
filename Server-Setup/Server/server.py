import asyncio, requests

# REST API URL of your LLM server
CHAT_URL = "http://192.168.12.141:8000/chat"  # Update IP

async def get_response(text, model):
    response = await requests.post(CHAT_URL, json={"message": text})
    return response.json()["response"]

async def listen():
    text = ""
    return text

async def speak(text):
    pass

async def get_states():
    tilt = x = y = z = None
    return [tilt, x, y, z]