import requests

from bs4 import BeautifulSoup
from duckduckgo_search import DDGS

def get_wikipedia_link(query):
    try:
        results = DDGS().text(query + " site:wikipedia.org", max_results=1)
        for result in results:
            link = result.get("href", "")
            if "wikipedia.org/wiki" in link:
                return link
        return None
    except Exception as e:
        raise e

          

def scrape_wikipedia_summary(url):
    response = requests.get(url)
    if response.status_code != 200:
        return "Failed to fetch Wikipedia page."

    soup = BeautifulSoup(response.text, "html.parser")
    
    title = soup.find("title")
    if not title:
        return "Failed to find the title on the Wikipedia page."

    content_div = soup.find("div", {"id": "bodyContent"})
    text = content_div.get_text(separator=' ', strip=True)
    if not text:
        return "Failed to find the paragraph on the Wikipedia page."

    return f"Title: {title.text.strip()}\n\n{text}"

def search_and_summarize(query):
    wiki_url = get_wikipedia_link(query)
    return scrape_wikipedia_summary(wiki_url), wiki_url
   