import requests
from bs4 import BeautifulSoup

def search_web(query):
    print(f"Gurk: Searching the web for '{query}'...")
    try:
        url = f"https://html.duckduckgo.com/html/?q={query.replace(' ', '+')}"
        headers = {"User-Agent": "Mozilla/5.0"}
        r = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(r.text, "html.parser")
        results = soup.find_all("a", class_="result__a")
        links = [a.get_text() for a in results][:5]
        return " | ".join(links) if links else "No results found."
    except Exception as e:
        return f"Search failed: {e}"
