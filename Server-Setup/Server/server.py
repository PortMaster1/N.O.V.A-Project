import asyncio, requests, re
from flask import Flask, request, jsonify
import llm_system

get_response = llm_system.get_response

app = Flask(__name__)

states = {
    "x": 0.0,
    "y": 0.0,
    "z": 0.0,
    "tilt": 0.0
}

def get_states():
    return states

@app.route("/")
async def root():
    return {"message": "Hello World"}

@app.route("/state", methods=["POST"])
async def receive_states():
    state = request.get_json()['state']
    global states
    x, y, z, tilt = state.split()
    statss.x = x
    states.y = y
    states.z = z
    states.tilt = tilt
    return {"message": "States Received"}

@app.route("/chat", methods=["POST"])
async def chat():
    message = request.get_json()['message']
    print(message)
    match = re.search("nova, sleep", message.lower())
    if match:
        # await rest.sleep_cycle()
        pass # TODO: FIX LATER
    else:
        response = await get_response(message)
    return {"response": response}
