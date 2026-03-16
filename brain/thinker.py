import random
from brain.reasoning import analyze
from brain.knowledge import search_memory

personality = [
    "humans fascinating creatures.",
    "thinking in progress.",
    "chaos but logical.",
    "interesting observation.",
]

def think(user_input):

    # analyze question
    intent = analyze(user_input)

    # check memory
    past = search_memory(user_input)

    if past:
        return f"I remember something similar: {past}"

    if intent == "greeting":
        return "hello human. gurk online."

    if intent == "identity":
        return "I am Gurk. experimental AI mind."

    if intent == "definition":
        return f"{random.choice(personality)} answer unclear but exploring."

    if intent == "reasoning":
        return "because reality is complex and humans ask strange questions."

    if intent == "instruction":
        return "step 1: think. step 2: test. step 3: improve."

    return random.choice(personality) + " elaborate."
