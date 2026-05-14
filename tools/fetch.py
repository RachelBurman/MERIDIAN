import feedparser
import requests
import logging
import pypdf
import tempfile

#Pull the FCA's RSS feed and return a list of items
#each item should have a title, URL, and publication date at minimum.
#feedparse
def fetch_feed(url: str):
    try: 
        d = feedparser.parse(url)
        results = []
        for entry in d.entries:
            results.append({"title": entry.title, "url": entry.link, "published_date": entry.published, "category": entry.tags[0]["term"] if entry.tags else "unknown"})
        return results
    except Exception as e:
        logging.error(f"Failed to fetch feed: {e}")
        return []
#Take a URL, fetch the actual page content, and return the text. 
#Some FCA documents are HTML, some are PDFs — for now let's handle HTML only and we'll add PDF handling after. 
#requests.
def fetch_document(url: str):
    try:
        response = requests.get(url, timeout=10)
        if url.endswith(".pdf"):
            with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
                tmp.write(response.content)
                tmp_path = tmp.name
                reader = pypdf.PdfReader(tmp_path)
                text = ""
                for page in reader.pages:
                    text += page.extract_text()
            return text
        else:
            return response.text
    except Exception as e:
        logging.error(f"Failed to fetch document: {e}")
        return None
    
