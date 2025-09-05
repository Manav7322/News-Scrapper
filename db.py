import sqlite3
from datetime import datetime

DB_NAME="news.db"

def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS headlines (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        source TEXT,
                        headline TEXT,
                        url TEXT,
                        scraped_at TEXT
                   )''')
    conn.commit()
    conn.close()

def insert_headline(source, headline, url):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO headlines (source, headline, url, scraped_at) VALUES (?, ?, ?, ?)",
                   (source, headline, url, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()
