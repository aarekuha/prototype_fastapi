import logging
import uvicorn
# from typing import Optional
from fastapi import FastAPI
from starlette.responses import Response
# from starlette.responses import JSONResponse
from starlette.requests import Request

from config import config

logging.getLogger("uvicorn.access").setLevel("WARN")
logging.basicConfig(level=config.LOG_LEVEL, format=config.LOG_FORMAT)
logger = logging.getLogger(__name__)

app = FastAPI(
    title=config.APP_TITLE,
    description=config.APP_DESCRIPTION,
    version=config.APP_VERSION,
    openapi_tags=config.TAGS_METADATA
)


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}


@app.middleware("http")
async def add_access_logging(request: Request, call_next):
    response: Response = await call_next(request)
    logger.info(f'{request.client.host}:{request.client.port} - '
                f'{request.method} {request.url} {response.status_code}')
    return response


"""
routers = [get_router, update_router, delete_router]
for router in routers:
    app.include_router(
        router,
        prefix="/api/v1",
        # dependencies=[Depends(get_token_header)],
        responses={
            #  401: {"description": config.HTTP_401},  # Invalid token
            422: {"description": config.HTTP_422},  # Invalid parameters
        },
    )
"""


if __name__ == '__main__':
    uvicorn.run(app, host=config.APP_HOST, port=int(config.APP_PORT), log_config=None)
