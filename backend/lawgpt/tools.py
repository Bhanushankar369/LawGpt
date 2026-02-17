from langchain_community.utilities import WikipediaAPIWrapper
from ddgs import DDGS

wiki = WikipediaAPIWrapper()

def wikipedia_search(query: str):
    return wiki.run(query)

def duckduckgo_search(query: str):
    results = []
    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=3):
            results.append(r["href"])
    return results
