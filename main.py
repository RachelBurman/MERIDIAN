import logging
import time
from agent import run_agent
import schedule

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def job():
    logging.info("Starting MERIDIAN...")
    start = time.time()
    run_agent()
    end = time.time()
    logging.info(f"Briefing complete in {round(end - start, 2)} seconds.")

schedule.every().day.at("08:00").do(job)
schedule.every().day.at("17:00").do(job)

# keep the script alive
while True:
    schedule.run_pending()
    time.sleep(60)