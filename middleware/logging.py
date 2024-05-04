from datetime import datetime
from fastapi import Request
async def logging(request: Request, call_next):
    start_time = datetime.now()
    response = await call_next(request)
    process_time = datetime.now() - start_time
    print(f"Request to {request.url.path} took {process_time} seconds")
    return response