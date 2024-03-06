import os

import monkey

def get_bot_token():
    return os.getenv('BOT_TOKEN')

def get_prefix():
    return eval(os.getenv('BOT_PREFIX', "['/monkey ', '/mk ']"))