# 📰 Automated News Scraper

A Python project that **scrapes headlines** from multiple news sites, **stores them in SQLite**, and **runs automatically on schedule** using Windows Task Scheduler.

---

## 📌 Features
- Scrapes headlines from:
  - [Hacker News](https://news.ycombinator.com)
  - [BBC News](https://www.bbc.com/news)
- Stores results in a local **SQLite database** (`news.db`)
- Each headline includes:
  - Source name
  - Headline text
  - Article URL
  - Timestamp of scraping
- Scheduled automation:
  - Runs automatically every day (or every N minutes) using **Task Scheduler**
- Prevents manual running — works in the background

---

## 🛠️ Tech Stack
- **Python 3.13**
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/) – HTML parsing
- [Requests](https://docs.python-requests.org/) – HTTP requests
- **SQLite** – lightweight database
- **Task Scheduler (Windows)** – automation

---

## 📂 Project Structure
```
news-scraper/
├── websites/
│   ├── bbc.py          # BBC scraper logic
│   ├── hackernews.py   # Hacker News scraper logic
├── db.py               # Database (create table + insert)
├── scraper.py          # Main runner script
├── requirements.txt    # Dependencies
├── README.md           # Documentation
└── screenshots/        # Setup & output screenshots
```

---

## ⚡ Setup & Installation

1. Clone this repo:
   ```bash
   git clone https://github.com/Manav7322/News-Scrapper.git
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Usage

Run manually:
```bash
python scraper.py
```

The script will:
- Scrape top headlines from BBC + Hacker News
- Store them in `news.db`
- Print latest entries in the console

---

## ⏰ Automation (Windows Task Scheduler)

1. Open **Task Scheduler** → Create Task
2. In **Triggers** → Set to run every day or every 5 minutes
3. In **Actions**:
   - Program/script: path to your `python.exe`
   - Add arguments: `"D:\path\to\scraper.py"`
   - Start in: `D:\path\to\project\`
4. Save & Run ✅

Now the scraper runs automatically!

---

## 🖼️ Screenshots
- Example database entries  
- Task Scheduler setup  
- Script running output  

*(add your screenshots in `/screenshots` folder)*

---

## 🚀 Future Improvements
- Add more news sources (NYTimes, Reuters, etc.)
- Prevent duplicate entries
- Export headlines to CSV/Excel
- Build a simple dashboard with Flask/Streamlit

---

## 📌 Author
👨‍💻 Manav Gupta 
Passionate about **Python development, automation, and data engineering**.
