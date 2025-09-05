import requests
from bs4 import BeautifulSoup

def scrape_bbc():
    url = "https://www.bbc.com/news"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    headlines = []
    for h in soup.select("h2[data-testid='card-headline']")[:5]:
        title = h.get_text(strip=True)
        parent_a = h.find_parent("a")
        link = None
        if parent_a and parent_a.get("href"):
            link = parent_a["href"]
            if link.startswith("/"):
                link = "https://www.bbc.com"+link
        headlines.append((title, link if link else "N/A"))
    return headlines

# print(scrape_bbc())