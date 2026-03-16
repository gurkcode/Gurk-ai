import requests
from bs4 import BeautifulSoup

def search_web(query):
    """
    Simple web search using DuckDuckGo.
    Returns a list of top 5 result titles.
    """
    url = f"https://duckduckgo.com/html/?q={query}"

    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    results = []

    for a in soup.select(".result__a")[:5]:
        results.append(a.get_text())

    return results
