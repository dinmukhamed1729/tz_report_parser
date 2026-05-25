import asyncio
from src.core.orchestrator import ReportOrchestrator
from src.utils.logger import setup_logger

async def main():
    setup_logger()
    orchestrator = ReportOrchestrator()
    await orchestrator.run()

if __name__ == "__main__":
    asyncio.run(main())