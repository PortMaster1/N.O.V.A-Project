import asyncio, requests

# Sender REST API URL of your LLM server
SERVER_URL = "http://192.168.12.141:8000/chat"  # Update IP

# Receiver REST API URL of the LLM server
RECEIVE_URL = "http://192.168.12.141:8000/state" # Update IP

# Talk to server
def talk_to_server(message):
    response = requests.post(SERVER_URL, json={"message": message})
    return response.json()["response"]

async def listen():
    text = ""
    return text

async def speak(text):
    pass

async def get_states():
    tilt = x = y = z = None
    return [tilt, x, y, z]