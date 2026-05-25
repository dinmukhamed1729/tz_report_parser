import requests
from src.config.settings import settings
from src.utils.logger import log


class ReportService:
    def fetch_report(self) -> dict:
        headers = {settings.API_KEY_NAME: settings.API_KEY}

        log.info("Запрос отчёта из API...")
        response = requests.get(settings.REPORT_URL, headers=headers, timeout=30)

        if response.status_code != 200:
            log.error(f"Ошибка API: {response.status_code} - {response.text}")
            response.raise_for_status()

        data = response.json()
        log.info(f"Отчёт успешно получен. Записей: {data.get('data', {}).get('total', 0)}")
        return data