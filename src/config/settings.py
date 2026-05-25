import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # API
    API_KEY = os.getenv("API_KEY")
    REPORT_URL = "https://middleware-01.fromtech.kz/test_report_dev/test_report"
    HEALTH_URL = "https://middleware-01.fromtech.kz/test_report_dev/health"

    # Telegram
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
    TELEGRAM_CHAT_IDS = [
        int(x.strip())
        for x in os.getenv("TELEGRAM_CHAT_IDS", "1459561428").split(",")
        if x.strip()
    ]

    # Email
    EMAIL_FROM = os.getenv("EMAIL_FROM")
    EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
    EMAIL_RECIPIENTS = [
        email.strip()
        for email in os.getenv("EMAIL_RECIPIENTS", "ykuzmin@fromtech.ru").split(",")
        if email.strip()
    ]

    # SMTP
    SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
    SMTP_PORT = int(os.getenv("SMTP_PORT", 587))

settings = Settings()