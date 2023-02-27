import random
import webbrowser


def get_response(message:str) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hey there'

    if p_message == 'bye':
        return 'bye'



