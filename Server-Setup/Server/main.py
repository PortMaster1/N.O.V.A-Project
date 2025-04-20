from server import listen, get_states
import re
from time import sleep
from memory_lane import remember, forget
import rest
import asyncio


# Real Loop
def main_loop():
    while True:
        user_input = listen()
        match = re.search('sleep', user_input.lower())
        if match:
            rest.sleep_cycle()
        response = get_response(user_input)
        speak(respomse)
        sleep(0.1)

# Old Loop
def main_loop():
    user_input = server.listen()
    response = get_response(user_input)
    for search in [r'\[REMEMBER: (.*?)\]', r'\[FORGET: (.*?)\]']:
        match = re.search(search, response)
        if match:
            text = match.group(1).split()
            action = text[0]
            args = text[1:]
            ## TODO: ADD IFs TO RUN FUNCTIONS
    server.send_to_client(edited_response)