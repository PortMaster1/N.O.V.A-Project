import asyncio, requests
from fastapi import FastAPI
from llm_system import get_response
import sensors

app = FastAPI()

old_text = ""
text = ""
states = {
    "x": 0.0,
    "y": 0.0,
    "z": 0.0,
    "tilt": 0.0
}

def _get_old_text():
    return old_text

def _get_text():
    return text

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

@app.post("/listen/{text}")
async def listen_api(user_input=""):
    global text
    text = user_input
    return {"message": "Text Received"}

@app.post("/chat/{message}")
async def chat(message):
    response = get_resposnse(message)
    return response

async def wait_until_unequal(func1, func2, check_interval=0.1):
    while func1() == func2():
        await asyncio.sleep(check_intetval)

async def listen():
    if _get_old_text() == _get_text():
        await wait_until_unequal(_get_old_text, _get_text)
    old_text = _get_text()
    return _get_text()