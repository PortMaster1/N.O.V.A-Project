from llm-system import get_response
import server
import re
from memory-lane import remember, forget





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