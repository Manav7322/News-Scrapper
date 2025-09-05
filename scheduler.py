import schedule
import time
from scraper import run_scraper

#Run scraper every day at 09:00 AM
schedule.every(1).minute.do(run_scraper)

print("⏳ Scheduler started... Press CTRL+C to stop")

while True:
    schedule.run_pending()
    time.sleep(1)