import smtplib
import os
import logging
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv

load_dotenv()

def send_briefing(filepath: str) -> None:
    try:
        gmail = os.getenv("GMAIL_ADDRESS")
        password = os.getenv("GMAIL_APP_PASSWORD")
        recipient = os.getenv("GMAIL_RECIPIENT")

        msg = MIMEMultipart()
        msg["Subject"] = "MERIDIAN Regulatory Briefing"
        msg["From"] = gmail
        msg["To"] = recipient

        with open(filepath, "rb") as f:
            attachment = MIMEBase("application", "octet-stream")
            attachment.set_payload(f.read())
            encoders.encode_base64(attachment)
            attachment.add_header("Content-Disposition", f"attachment; filename={os.path.basename(filepath)}")
            msg.attach(attachment)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(gmail, password)
            server.send_message(msg)
            logging.info("Briefing emailed successfully.")

    except Exception as e:
        logging.error(f"Failed to email briefing: {e}")