from fastapi import FastAPI
import uvicorn

from hpc_service.app.api.api_v1.api import api_router
from hpc_service.app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME,
              openapi_url=f"{settings.API_V1_STR}/openapi.json")

app.include_router(api_router, prefix=settings.API_V1_STR)


def start():
    uvicorn.run("hpc_service.app.main:app", host="0.0.0.0", port=8888, reload=True)
