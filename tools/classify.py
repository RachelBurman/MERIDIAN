from config import DOMAINS


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
        "news_stories": 1,
        "dear_ceo": 4,
    }
    score = type_map.get(doc_type.lower(), 1)

    if any(tag in DOMAINS for tag in domain_tags) and score < 5:
        score += 1

    return score


