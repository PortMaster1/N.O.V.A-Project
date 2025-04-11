from llm_system import get_response
import server
import re
from memory_lane import remember, forget





def main_loop():
    user_input = server.listen()
    response = get_response(user_input)
    match = re.search(r'\[REMEMBER: (.*?)\]', response)
    if match:
        text = match.group(1).split()
        action = text[0]
        args = text[1:]
        if action == "turn_head":
    
    match = re.search(r'\[FORGET: (.*?)\]', response)
    if match:
        text = match.group(1).split()
        action = text[0]
        args = text[1:]
        if action == "turn_head":
                
            ## TODO: ADD IFs TO RUN FUNCTIONS
    server.send_to_client(edited_response)