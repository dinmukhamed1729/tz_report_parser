import asyncio
from src.services.report_service import ReportService
from src.services.phone_service import PhoneService
from src.services.excel_service import ExcelService
from src.services.email_service import EmailService
from src.services.telegram_service import TelegramService
from src.utils.logger import log


class ReportOrchestrator:
    def __init__(self):
        self.report_service = ReportService()
        self.phone_service = PhoneService()
        self.excel_service = ExcelService()
        self.email_service = EmailService()
        self.telegram_service = TelegramService()

    async def run(self):
        log.info("=== Запуск процесса обработки отчёта ===")
        await self.telegram_service.notify_start()

        try:
            report = self.report_service.fetch_report()
            phones = self.phone_service.extract_unique_phones(report)

            if not phones:
                log.warning("Уникальные номера не найдены")
                await self.telegram_service.notify_success(0, "Нет данных")
                return

            file_path = self.excel_service.create_excel(phones)
            await self.email_service.send_email(file_path, len(phones))

            await self.telegram_service.notify_success(len(phones), file_path)
            log.info("=== Скрипт успешно завершён ===")

        except Exception as e:
            log.error(f"Критическая ошибка: {e}", exc_info=True)
            await self.telegram_service.notify_error(e)