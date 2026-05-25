from loguru import logger
import sys
from datetime import datetime

def setup_logger():
    logger.remove()
    logger.add(
        sys.stdout,
        format="<green>{time:HH:mm:ss}</green> | <level>{level}</level> | {message}",
        level="INFO"
    )
    logger.add(
        f"logs/app_{datetime.now().strftime('%Y-%m-%d')}.log",
        rotation="10 MB",
        retention="7 days",
        level="DEBUG"
    )
    return logger

log = setup_logger()