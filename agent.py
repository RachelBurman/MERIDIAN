from config import URGENCY_THRESHOLD, FCA_FEED_URL
from db import initialise_db, is_seen, store_document
from tools.brief import generate_briefing
from tools.fetch import fetch_document, fetch_feed
from tools.summarise import summarise_document
from tools.classify import classify_type, score_urgency

def run_agent():
    initialise_db()
    entries = fetch_feed(FCA_FEED_URL)
    
    for i in entries:
        if is_seen(i["url"]):
            continue
        else: 
            doc_type = classify_type(i["category"])
            urgency = score_urgency(doc_type, [])
            if urgency >= URGENCY_THRESHOLD:
                text = fetch_document(i["url"])
                summary = summarise_document(text, doc_type)
            else: 
                summary = None
            
            store_document(i["url"], i["title"], doc_type, "", urgency, summary, "FCA", i["published_date"])
   
    generate_briefing()
    

             


