from brain.memory import load_memory

def search_memory(user_input):

    memory = load_memory()

    for m in reversed(memory):

        if user_input.lower() in m["human"].lower():
            return m["Gurk"]

    return None
