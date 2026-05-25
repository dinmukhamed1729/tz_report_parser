import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path

from src.config.settings import settings
from src.utils.logger import log


class EmailService:
    def __init__(self):
        self.from_email = settings.EMAIL_FROM
        self.password = settings.EMAIL_PASSWORD
        self.to_emails = settings.EMAIL_RECIPIENTS
        self.smtp_server = settings.SMTP_SERVER
        self.smtp_port = settings.SMTP_PORT

    async def send_email(self, file_path: str, phone_count: int):
        if not self.from_email or not self.password or not self.to_emails:
            log.warning("Email credentials not fully configured. Skipping email sending.")
            return

        try:
            log.info(f"Подготовка отправки письма на {len(self.to_emails)} получателя(ей)")

            msg = MIMEMultipart()
            msg['From'] = self.from_email
            msg['To'] = ", ".join(self.to_emails)
            msg['Subject'] = f"Отчёт по уникальным номерам — {phone_count} шт. ({Path(file_path).name})"

            body = f"""
            Добрый день!

            Скрипт успешно выполнен.
            Найдено уникальных номеров телефонов: {phone_count}

            Во вложении файл с уникальными номерами.
            """

            msg.attach(MIMEText(body, 'plain'))

            # Прикрепляем Excel файл
            filename = Path(file_path).name
            with open(file_path, "rb") as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f'attachment; filename={filename}')
                msg.attach(part)

            # Отправка
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.from_email, self.password)
                server.send_message(msg)

            log.info(f"✅ Письмо успешно отправлено на: {', '.join(self.to_emails)}")

        except Exception as e:
            log.error(f"Ошибка при отправке email: {e}", exc_info=True)
            raise