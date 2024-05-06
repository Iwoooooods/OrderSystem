from datetime import datetime, date
from fastapi import Request
from loguru import logger

async def logging(request: Request, call_next):
    start_time = datetime.now()
    response = await call_next(request)
    process_time = datetime.now() - start_time
    logger.info(f"Request to {request.url.path} took {process_time} seconds")
    return response

async def create_log_file():
    logger.add(f'{date.today().strftime(format="%Y%m%d")}.log', level="DEBUG")

