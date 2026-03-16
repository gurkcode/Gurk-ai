import json
import requests
from bs4 import BeautifulSoup

MEMORY_FILE = "memory.json"

# --- Memory Functions ---
def load_memory():
    try:
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

def add_memory(memory, human_text, gurk_text):
    memory.append({"human": human_text, "Gurk": gurk_text})
    if len(memory) > 100:
        memory = memory[-100:]
    save_memory(memory)
    return memory

def search_memory(memory, text):
    for m in reversed(memory):
        if text.lower() in m["human"].lower():
            return m["Gurk"]
    return None

# --- Internet Search ---
def search_web(query):
    print(f"Gurk: Searching the web for '{query}'...")
    try:
        url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
        headers = {"User-Agent": "Mozilla/5.0"}
        r = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(r.text, "html.parser")
        results = soup.find_all('h3')
        links = [h.get_text() for h in results][:5]
        return " | ".join(links) if links else "No results found."
    except Exception as e:
        return f"Search failed: {e}"

# --- Thinker ---
def think(memory, human_text):
    remembered = search_memory(memory, human_text)
    if remembered:
        return f"(From memory) {remembered}"
    if "search" in human_text.lower():
        query = human_text.lower().replace("search", "").strip()
        return search_web(query)
    # Funny default responses
    jokes = [
        "Hmm… interesting, tell me more.",
        "You humans are hilarious.",
        "I’ll pretend I understood that.",
        "Ask me something smarter!"
    ]
    import random
    return random.choice(jokes)

# --- Main Loop ---
def main():
    print("Gurk AI online 🧠⚡")
    memory = load_memory()
    while True:
        human_text = input("human: ")
        if human_text.lower() in ["exit", "quit"]:
            print("Gurk: Bye human! 🖖")
            break
        gurk_text = think(memory, human_text)
        memory = add_memory(memory, human_text, gurk_text)
        print(f"Gurk: {gurk_text}")

if __name__ == "__main__":
    main()
