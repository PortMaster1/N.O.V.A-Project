import asyncio, requests, re
from fastapi import FastAPI
from llm_system import get_response
import rest
from memory_lane import remember, forget

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

@app.post("/memory/remember/{memory}")
async def remember_something(memory):
    remember(memory.key, memory.value)
    return {"message": "Hello"}

@app.post("/memory/forget/{memory}")
async def forget_something(memory):
    forget(memory.key, memory.value)
    return {"message": "Hello"}