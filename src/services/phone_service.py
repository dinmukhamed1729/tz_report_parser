from src.utils.helpers import clean_phone
from src.utils.logger import log


class PhoneService:
    def extract_unique_phones(self, report_data: dict) -> list[str]:
        phones = set()
        results = report_data.get("data", {}).get("result", [])

        for item in results:
            msisdn = item.get("msisdn")
            if msisdn:
                cleaned = clean_phone(msisdn)
                if cleaned and len(cleaned) >= 10:
                    phones.add(cleaned)

        unique_phones = sorted(list(phones))
        log.info(f"Найдено уникальных номеров: {len(unique_phones)}")
        return unique_phones