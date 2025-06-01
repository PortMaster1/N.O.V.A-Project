import asyncio, requests
# Testing Imports
import asyncio, socket, signals

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

HOST = "192.168.12.138"
PORT = "8080"

signals = signals.Signals()

class Client:
    def __init__(self, HOST, PORT):
        self._HOST = HOST
        self._PORT = PORT
        # Initialize Socket Server
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    async def start_listening(self):
        self.s.connect(self._HOST, self._PORT)
        while True:
            data = self.s.recv(1024).decode()
            print("Received: " + data)
    
    async def send(self, data):
        encoded = data.encode()
        self.s.sendall(encoded)