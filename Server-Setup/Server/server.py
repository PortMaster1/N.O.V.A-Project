import asyncio, requests
from fastapi import FastAPI
from llm_system import get_response
import sensors

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/state/{states}")
async def get_states(states=[]):
    x, y, z, tilt = states
    return {"message": "States Received"}

@app.post("/chat/{message}")
async def chat(message):
    response = get_resposnse(message)
    return response


async def listen():
    text = ""
    return text

async def speak(text):
    pass

async def get_states():
    tilt = x = y = z = None
    return [tilt, x, y, z]