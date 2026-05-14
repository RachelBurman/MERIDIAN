import requests
import logging

def summarise_document(text: str, doc_type: str)->str:
    if not text: 
     return None
        
    prompt = f"""You are a regulatory intelligence assistant.
                Summarise the following FCA {doc_type} in exactly three sentences:
                1. What this document is and what it covers
                2. Who it affects
                3. What action is required, if any

                Document:
                {text[:3000]}"""
    
    
    try:
        response = requests.post("http://localhost:11434/api/generate", json={
        "model": "qwen2.5:latest",
        "prompt": prompt,
        "stream": False
        })
        return response.json()["response"]
    except Exception as e:
        logging.error(f"Failed to summarise: {e}")
        return None
                    



