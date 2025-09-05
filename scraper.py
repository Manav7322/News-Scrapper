from db import create_table, insert_headline

from websites.hacker_News import scrape_hackernews
from websites.bbc import scrape_bbc

def run_scraper():
    create_table()

    #scrape hacker news 
    for text, url in scrape_hackernews():
        insert_headline("Hacker News", text, url)

    #scrape BBC
    for text, url in scrape_bbc():
        insert_headline("BBC", text, url)

    print("✅ Headlines scraped and saved to DB")

if __name__ == "__main__":
    run_scraper()
    