import requests

from bs4 import BeautifulSoup
from duckduckgo_search import DDGS

def get_wikipedia_link(query):
    results = DDGS().text(query + " site:wikipedia.org", max_results=5)
    for result in results:
        link = result.get("href", "")
        if "wikipedia.org/wiki" in link:
            return link
    return None


def scrape_wikipedia_summary(url):
    response = requests.get(url)
    if response.status_code != 200:
        return "Failed to fetch Wikipedia page."

    soup = BeautifulSoup(response.text, "html.parser")
    
    title = soup.find("h1")
    if not title:
        return "Failed to find the title on the Wikipedia page."

    content_div = soup.find("div", {"class": "mw-parser-output"})
    if not content_div:
        return "Failed to find the content div on the Wikipedia page."

    first_para = content_div.find("p", recursive=False)
    if not first_para:
        return "Failed to find the first paragraph on the Wikipedia page."

    return f"Title: {title.text.strip()}\n\n{first_para.text.strip()}"

def search_and_summarize(query):
    wiki_url = get_wikipedia_link(query)
    if not wiki_url:
        return "No Wikipedia page found in search results."
    return scrape_wikipedia_summary(wiki_url)