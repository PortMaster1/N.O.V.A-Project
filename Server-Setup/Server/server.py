import asyncio, requests, re
from flask import Flask, request, jsonify, render_template
from llm_system import *
# Testing Imports
import asyncio
import websockets
import json

# Set up functions because Python is weird
"""
get_response is from llm_system
get_chat_mem is from llm_system
"""

app = Flask(__name__)

def get_states():
	return states
	
@app.route("/")
async def root():
	return {"message": "Hello World"}
	
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
	return render_template("index.html", chat_mem=chat_mem)
	
# Start Testing Here:

HOST = "0.0.0.0"
PORT = 1052
URL = f"ws://{HOST}:{PORT}"


class Server:
	def __init__(self, host, port):
		self._HOST = host
		self._PORT = port
		self.clients = set()
	
	
	async def handler(self, websocket, path):
		print("Client Connected")
		self.clients.add(websocket)
		try:
			async for message in websocket:
				message = json.dumps(message, indent=2)
				print("Received: " + message)
		except websockets.ConnectionClosed:
			print("Client Disconnected")
		finally:
			self.clients.remove(websocket)
	
	
	async def send(self, data):
		data = json.loads(data)
		for client in self.clients:
			await client.send(data)
		print(f"Sent data to client(s)")
	
	
	async def start(self):
		print(f"Starting Websocket on ws://{self._HOST}:{self._PORT}")
		async with websockets.serve(self.handler, self._HOST, self._PORT):
			await asyncio.Future() # Run Forever

if __name__ == "__main__":
	server = Server()
	asyncio.run(server.start())