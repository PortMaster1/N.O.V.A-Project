import asyncio, requests, re
from fastapi import FastAPI
from . import llm_system
from . import rest

get_response = llm_system.get_response

app = FastAPI()

states = {
    "x": 0.0,
    "y": 0.0,
    "z": 0.0,
    "tilt": 0.0
}

def get_states():
    return states

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/state/{state}")
async def receive_states(state=[]):
    global states
    x, y, z, tilt = state
    statss.x = x
    states.y = y
    states.z = z
    states.tilt = tilt
    return {"message": "States Received"}

@app.post("/chat/{message}")
async def chat(message):
    match = re.search("nova, sleep", message.lower())
    if match:
        await rest.sleep_cycle()
    else:
        response = get_resposnse(message)
    return response
