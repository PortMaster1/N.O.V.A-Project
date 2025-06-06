import asyncio, requests
# Testing Imports
import asyncio, socket

# REST API URL of your LLM server
IP = "192.168.12.138:8000"            # Update IP Address
CHAT_URL = f"http://{IP}/chat"
STATE_URL = f"http://{IP}/state"

def get_response(text, model="day_model"):
    response = requests.post(CHAT_URL, json={"message": text})
    return response.json()["response"]

async def send_states(x, y, z, tilt):
    requests.post(STATE_URL, json={"states": [x, y, z, tilt]})
    return

# Testing Starts Here

HOST = "192.168.12.140"
PORT = 8080

class Client:
    def __init__(self, HOST, PORT, signals):
        self._HOST = HOST
        self._PORT = PORT
        self.signals = signals
        # Initialize Socket Server
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def start_listening(self):
        self.s.connect(self._HOST, self._PORT)
        while True:
            data = self.s.recv(1024).decode()
            print("Received: " + data)
            # Include a match statement here
    
    def send(self, data):
        encoded = data.encode()
        self.s.sendall(encoded)
    
    def socket_loop(self):
        while not self.signals.terminate:
            self.start_listening()