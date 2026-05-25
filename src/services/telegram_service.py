from telegram import Bot
from src.config.settings import settings
from src.utils.logger import log

class TelegramService:
    def __init__(self):
        self.bot = Bot(token=settings.TELEGRAM_TOKEN)
        self.chat_ids = settings.TELEGRAM_CHAT_IDS

    async def _send_to_all(self, text: str):
        for chat_id in self.chat_ids:
            try:
                await self.bot.send_message(chat_id, text, parse_mode="HTML")
            except Exception as e:
                log.error(f"Не удалось отправить уведомление в чат {chat_id}: {e}")

    async def notify_start(self):
        await self._send_to_all("🚀 Скрипт запущен — получение отчёта...")

    async def notify_success(self, count: int, file_path: str):
        await self._send_to_all(
            f"✅ Успешно выполнено!\n"
            f"Найдено уникальных номеров: <b>{count}</b>\n"
            f"Файл: <code>{file_path}</code>"
        )

    async def notify_error(self, error: Exception):
        await self._send_to_all(
            f"❌ Ошибка при выполнении скрипта:\n<code>{str(error)[:400]}</code>"
        )