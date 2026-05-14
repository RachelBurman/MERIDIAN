import time
from agent import run_agent

print("Starting MERIDIAN...")
start = time.time()
run_agent()
end = time.time()
print(f"Briefing complete in {round(end - start, 2)} seconds.")