import logging
import time
from agent import run_agent

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Starting MERIDIAN...")
start = time.time()
run_agent()
end = time.time()
logging.info(f"Briefing complete in {round(end - start, 2)} seconds.")