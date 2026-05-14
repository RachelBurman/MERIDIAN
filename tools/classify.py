from config import DOMAINS, KEYWORDS


def classify_type(category: str) -> str:
    type_map = {
        "policy statement": "policy_statement",
        "consultation paper": "consultation_paper",
        "enforcement": "enforcement",
        "guidance": "guidance",
        "newsletter": "newsletter",
        "speeches": "speeches",
        "news stories": "news_stories",
        "dear ceo": "dear_ceo",
        "blogs": "blogs",
        "press releases": "press_releases",
        "statements": "statements",
    }
    return type_map.get(category.lower(), "unknown")


def score_urgency(doc_type: str, domain_tags: list):
    type_map = {
        "policy_statement": 4,
        "consultation_paper": 3,
        "enforcement": 5,
        "guidance": 2,
        "newsletter": 1,
        "speeches": 3,
        "news_stories": 3,
        "dear_ceo": 4,
        "blog": 1,
        "press_releases": 3,
        "statements": 3,
    }
    score = type_map.get(doc_type.lower(), 1)

    if any(tag in DOMAINS for tag in domain_tags) and score < 5:
        score += 1

    return score

def classify_title(title: str, urgency: int) -> int:
    if any(keyword in title.lower() for keyword in KEYWORDS):
        urgency = 5
    return urgency
    
