import os
from db import get_recent_documents
from datetime import datetime, timezone

def generate_briefing():
    doc = get_recent_documents()
    high = []
    med = []
    low =[]
    for i in doc:
        if i[6] >= 4:     
            high.append(i)
        elif i[6] >= 2:
            med.append(i)
        else:
            low.append(i)

    content = f"# MERIDIAN Regulatory Briefing\n"
    content += f"## {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M')} UTC\n\n"
    content += "### 🔴 High Priority\n\n"
    for i in high:
        content += f"- Title: {i[3]}\n"
        content += f"- Type: {i[4]}\n"
        content += f"- Published: {i[9]}\n"
        content += f"- Summary: {i[7]}\n\n"  

    content += "### 🟡 Medium Priority\n\n"
    for i in med:
        content += f"- Title: {i[3]}\n"
        content += f"- Type: {i[4]}\n"
        content += f"- Published: {i[9]}\n"
        content += f"- Summary: {i[7]}\n\n" 

    content += "### 🟢 Low Priority\n\n"
    for i in low:
        content += f"- Title: {i[3]}\n"
        content += f"- Type: {i[4]}\n"
        content += f"- Published: {i[9]}\n"
        content += f"- Summary: {i[7]}\n\n" 

    filepath = f"briefings/meridian_{datetime.now(timezone.utc).strftime('%Y-%m-%d_%H%M')}.md"
    os.makedirs("briefings", exist_ok=True) 
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    return filepath

