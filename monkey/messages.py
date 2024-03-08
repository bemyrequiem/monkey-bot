import discord
import random

keywords = {
    "monkey": ["UU AA"],
    "banana": ["mmm bananas"]
}

def too_many_arguments():
    return "Too many arguments"

def check_keywords(text):
    for keyword in keywords.keys():
        if keyword in text:
            return random.choice(keywords[keyword])