import time
import logging
from fastapi import Request

logger = logging.getLogger("middleware.timer")

async def timer(request: Request, call_next):
    start = time.perf_counter()
    response = await call_next(request)
    duration = time.perf_counter() - start

    response.headers["X-Process-Time"] = f"{duration:.4f}"
    logger.info(
        "%s %s completed in %.4fs",
        request.method,
        request.url.path,
        duration,
    )
    return response
