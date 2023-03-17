from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException

from hpc_service.app.core.config import settings
from hpc_service.app.utils import ping

router = APIRouter()


@router.get("/ping_hpc")  # , response_model=List[schemas.Item] )
def ping_hpc() -> Any:
    pong = ping(settings.HPC_HOST)
    req = {"pong": pong}
    return req
