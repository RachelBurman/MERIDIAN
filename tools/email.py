import os
import logging
from dotenv import load_dotenv
import resend

load_dotenv()

resend.api_key = os.getenv("RESEND_API_KEY")


def send_briefing(filepath: str) -> None:
    try:
        with open(filepath, "rb") as f:
            attachment = {
                "filename": os.path.basename(filepath),
                "content": list(f.read())
            }
        resend.Emails.send({
        "from": os.getenv("RESEND_FROM"),
        "to": [os.getenv("RESEND_RECIPIENT")],
        "subject": "MERIDIAN Regulatory Briefing",
        "html": "<p>Your briefing is attached.</p>",
        "attachments": [attachment]
    })
        logging.info("Briefing emailed successfully.")


    except Exception as e:
        logging.error(f"Failed to email briefing: {e}")





