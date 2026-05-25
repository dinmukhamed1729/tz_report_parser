import pandas as pd
from datetime import datetime
from src.utils.logger import log


class ExcelService:
    def create_excel(self, phones: list[str]) -> str:
        df = pd.DataFrame({"phone": phones})

        filename = f"unique_phones_{datetime.now().strftime('%Y-%m-%d_%H-%M')}.xlsx"
        filepath = f"output/{filename}"

        df.to_excel(filepath, index=False)
        log.info(f"Excel-файл создан: {filepath}")
        return filepath
