import asyncio, requests
from time import sleep
from sensors import listen, speak#, read_microbit


"""
async def send_state_loop():
    while True:
        x, y, z, tilt = await read_microbit()
        await send_states(x, y, z, tilt)
        await asyncio.sleep(0.1)
"""

class Main:
    def __init__(self):
        while True:
            text = listen()
            reaponse = self.get_response(text)
            speak(response)
            sleep(0.1)
    
    def send_states(self, x, y, z, tilt):
        requests.post(STATE_URL, json={"states": [x, y, z, tilt]})
        return
    
    def get_response(self, text, model="day_model"):
        # REST API URL of your LLM server
        IP = "192.168.12.138:8000"            # Update IP Address
        CHAT_URL = f"http://{IP}/chat"
        STATE_URL = f"http://{IP}/state"
        response = requests.post(CHAT_URL, json={"message": text})
        return response.json()["response"]

async def llm_loop():
    while True:
        text = listen()
        response = await get_response(text)
        speak(response)
        await asyncio.sleep(0.1)

def main_loop():
    #asyncio.run(send_state_loop)
    #asyncio.run(llm_loop)
    m = Main()

if __name__ == "__main__":
    main_loop()
