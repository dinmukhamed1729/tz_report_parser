import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # API
    API_KEY = os.getenv("API_KEY")
    REPORT_URL = os.getenv("REPORT_URL")
    HEALTH_URL = os.getenv("HEALTH_URL")

    # Telegram
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
    TELEGRAM_CHAT_IDS = [
        int(x.strip())
        for x in os.getenv("TELEGRAM_CHAT_IDS").split(",")
        if x.strip()
    ]

    # Email
    EMAIL_FROM = os.getenv("EMAIL_FROM")
    EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
    EMAIL_RECIPIENTS = [
        email.strip()
        for email in os.getenv("EMAIL_RECIPIENTS").split(",")
        if email.strip()
    ]

    # SMTP
    SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
    SMTP_PORT = int(os.getenv("SMTP_PORT", 587))

settings = Settings()