import requests
from bs4 import BeautifulSoup

def scrape_hackernews():
    url = "https://news.ycombinator.com/"
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, "html.parser")

    headlines = []
    for h in soup.select("span.titleline > a")[:5]:
        headlines.append((h.get_text(strip=True), h["href"]))
    return headlines

# print(scrape_hackernews())