# This is MERIDIAN's memory
import sqlite3
import hashlib
from datetime import datetime, timezone, timedelta
# 1. create database and tables on first run
# On first run meridian.db does not exist. db.py creates and sets up the schema on every run after that, 
# it connects without breaking anything
# 2. Store a document record
# When the agent processes a document, it needs to save: URL; hash of URL (deduplication); document type;
# urgency score; source; publication date; summary; when meridian processed it
# 3. Check if a document has been seen before
# Before fetching, check hash - If it's in the database, skip it
# 4. Retrieve records for briefing generation
# Fetch documents processed in last N hours, ordered by urgency score descending
# Breifing always leads with what matters most


con = sqlite3.connect("data/meridian.db")
cur = con.cursor()

def hash_url(url: str) -> str:
    return hashlib.sha256(url.encode()).hexdigest()

def initialise_db():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY,
            url TEXT,
            url_hash TEXT UNIQUE,
            title TEXT,
            doc_type TEXT,
            domain_tags TEXT,
            urgency_score INTEGER,
            summary TEXT,
            source TEXT,
            published_date TEXT,
            processed_at TEXT
        )
    """)

    con.commit()



# What store_document() Needs To Do
# It takes all the information about a document, and inserts it as a row into the documents table. It should also:

# Generate the url_hash using your hash_url() function
# Generate the processed_at timestamp at the moment of storing
# Handle the case where a document with that hash already exists — not crash, just silently skip it

def store_document(url, title, doc_type, domain_tags, urgency_score, summary, source, published_date):
    
    urlhash = hash_url(url)
    
    processed_at = datetime.now(timezone.utc).isoformat()
    
    cur.execute("INSERT OR IGNORE INTO documents VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (url, urlhash, title, doc_type, domain_tags, urgency_score, summary, source, published_date, processed_at))

    con.commit()

def is_seen(url: str) -> bool:
    urlhash = hash_url(url)
    cur.execute("SELECT 1 FROM documents WHERE url_hash = ?", (urlhash,))
    return cur.fetchone() is not None

def get_recent_documents(hours: int = 24):
    t = datetime.now()
    res = t - timedelta(hours=hours)
    cur.execute("SELECT * FROM documents WHERE processed_at > ? ORDER BY urgency_score DESC", (res,))
    return cur.fetchall()

