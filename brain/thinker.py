import random

responses = [
    "humans confusing.",
    "internet loud today.",
    "thinking... maybe.",
    "chaos detected."
]

def think(user_input):
    base = random.choice(responses)
    return f"{base} you said: {user_input.lower()}"
---

## Run Guck
