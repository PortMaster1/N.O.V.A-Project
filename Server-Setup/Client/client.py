# Dalton Knapp
import asyncio
import websocket
import configparser
import threading

config = configparser.ConfigParser()
config.read('config.ini')
if config == []:
	raise FileNotFoundError()
config = config['DEFAULT']

class Client (threading.Thread):
	def __init__(self, host=None, port=None):
		super().__init__()
		self.connected = False
		if not host:
			self._HOST = config['server_address']
		if not port:
			self._PORT = int(config['server_port'])
	
	def run(self):
		self.ws = websocket.WebsocketApp(
			f"ws://{self._HOST}:{self._PORT}",
			on_open = self.on_open,
			on_message = self.on_message
		)
		self.ws.run_forever()
	
	def on_open(self, ws):
		print("Connected!")
	
	def on_message(self, ws, message):
		print(f"Received:\n{message}")
		# TODO: Match Stuff in another function
	
	def chat_message(prompt):
		data = json.loads({"type":"chat_cmd", "prompt":prompt})
		self.ws.send(data)


if __name__ == "__main__":
	print("Hi :)")