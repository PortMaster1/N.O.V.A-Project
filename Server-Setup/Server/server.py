import asyncio, requests
from fastapi import FastAPI
from llm_system import get_response
import sensors

app = FastAPI()

old_text = ""
text = ""

def _get_old_text():
    return old_text

def _get_text():
    return text

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/state/{states}")
async def get_states(states=[]):
    x, y, z, tilt = states
    return {"message": "States Received"}

@app.post("/listen/{text}")
async def listen_api(text=""):
    return text

@app.post("/chat/{message}")
async def chat(message):
    response = get_resposnse(message)
    return response

async def wait_until_equal(func1, func2, check_interval=0.1):
    pass

async def listen():
    if _get_old_text() == _get_text():
        await text != old_text
    else:
        old_text = text
    return text

async def speak(text):
    pass