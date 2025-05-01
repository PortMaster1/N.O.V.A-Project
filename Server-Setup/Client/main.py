import asyncio
from time import sleep
from server import send_states, get_response
from sensors import listen, speak#, read_microbit

"""
async def send_state_loop():
    while True:
        x, y, z, tilt = await read_microbit()
        await send_states(x, y, z, tilt)
        await asyncio.sleep(0.1)
"""

async def llm_loop():
    while True:
        text = listen()
        response = await get_response(text)
        speak(response)
        await asyncio.sleep(0.1)

def llm_placeholer_loop():
    while True:
        text = listen()
        response = get_response(text)
        speak(response)
        sleep(0.1)

def main_loop():
    #asyncio.run(send_state_loop)
    #asyncio.run(llm_loop)
    llm_placeholer_loop()
