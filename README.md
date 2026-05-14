# MERIDIAN 🔍

**An autonomous agent that monitors FCA publications, classifies by urgency, and delivers structured briefings.**

Regulatory agencies publish hundreds of documents a year and nobody has time to read it all. Meridian is a working agent that solves it by fetching, classifying, and briefing you on what actually matters.  As an agentic system, it scores each document from 1 (least urgent) to 5 (most urgent), based on document type and document title. If a document scores below 4, MERIDIAN stores the metadata only. If it scores 4 or 5, it fetches the full document, summarises it, and flags it for the briefing.

---

## How It Works

```
initialise db
↓
fetch FCA feed
↓
for each document:
    check if seen → skip if yes
    classify document type
    score urgency on document type
    score urgency on title keywords
    ↓
    if urgency >= threshold (4):
        fetch full document
        summarise document
    
    store document in db
↓
generate briefing
```

## Tech Stack

| Component | Technology |
|---|---|
| Language | Python 3.14 |
| LLM | Qwen 2.5 via Ollama |
| Database | SQLite |
| Feed Source | FCA RSS |
| Key Libraries | feedparser, requests, hashlib, datetime |

## Getting Started

**Prerequisites**
- Python 3.14+
- [Ollama](https://ollama.com) installed and running

```bash
# clone repo
git clone https://github.com/RachelBurman/MERIDIAN.git
cd MERIDIAN

# install dependencies
pip install requests feedparser

# pull the LLM
ollama pull qwen2.5:latest

# create data directory
mkdir data

# run MERIDIAN
python main.py
```

### Example Reports
Here is an example brief taken from 14/05/2026
[View example briefing](./examplebriefing.md)

## Roadmap

- [x] Core agentic pipeline — fetch, classify, summarise, brief
- [x] Title-based keyword urgency classification
- [x] Error handling and timeouts
- [ ] Scheduling — automated daily runs
- [ ] Domain tag matching — completes urgency scoring
- [ ] PDF handling — richer summaries from policy documents
- [ ] Email delivery — production ready briefings
- [ ] Logging — replace print statements with proper log levels


## About

Hi, I'm Rachel, a data scientist with a passion for AI and machine learning, currently working as a research assistant in data science and clinical trials.

[GitHub](https://github.com/RachelBurman) • [Personal Website](https://rachelburman.space)