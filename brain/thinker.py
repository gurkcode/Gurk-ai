import random

responses = [
    "humans confusing.",
    "internet loud today.",
    "thinking... maybe.",
    "chaos detected.",
    "logic unclear but interesting."
]

def think(user_input):
    return f"{random.choice(responses)} "
