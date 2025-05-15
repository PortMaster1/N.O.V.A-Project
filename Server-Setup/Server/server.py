import asyncio, requests, re
from flask import Flask, request, jsonify, render_template
import llm_system

# Set up functions because Python is weird
get_response = llm_system.get_response
get_chat_mem = llm_system.get_chat_mem

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

@app.route("/api/state", methods=["POST"])
async def receive_states():
    state = request.get_json()['state']
    global states
    x, y, z, tilt = state.split()
    statss.x = x
    states.y = y
    states.z = z
    states.tilt = tilt
    return {"message": "States Received"}

@app.route("/api/chat", methods=["POST"])
async def apichat():
    message = request.get_json()['message']
    print(message)
    match = re.search("nova, sleep", message.lower())
    if match:
        # await rest.sleep_cycle()
        pass # TODO: FIX LATER
    else:
        response = await get_response(message).content
    return {"response": response}

@app.route("/chat", methods=["GET","POST"])
async def chat():
    if request.method == "POST":
        message = request.get_form()['message']
        print(message)
        #response = get_response(message)
        response = "This is an example response and needs to be replaced in N.O.V.A-Project/Server-Setup/Server/server.py."
    chat_mem = get_chat_mem()
    return render_template("files/index.html", chat_mem=chat_mem)
