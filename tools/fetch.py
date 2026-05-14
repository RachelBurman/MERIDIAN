import feedparser
import requests
#Pull the FCA's RSS feed and return a list of items
#each item should have a title, URL, and publication date at minimum.
#feedparse
def fetch_feed(url: str):
    d = feedparser.parse(url)
    results = []
    for entry in d.entries:
        print(entry.tags)  # temporary debug line
        results.append({"title": entry.title, "url": entry.link, "published_date": entry.published, "category": entry.tags[0]["term"] if entry.tags else "unknown"})
    return results

#Take a URL, fetch the actual page content, and return the text. 
#Some FCA documents are HTML, some are PDFs — for now let's handle HTML only and we'll add PDF handling after. 
#requests.
def fetch_document(url: str):
    try:
        return requests.get(url).text
    except:
        return None
    
