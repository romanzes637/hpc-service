from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status, Response

from hpc_service.app.core.config import settings
from hpc_service.app.utils import ping, ssh_pbs, job_status

router = APIRouter()


@router.get("/ping_hpc")
def ping_hpc() -> Any:
    pong = ping(settings.HPC_HOST)
    return {"pong": pong}
  

@router.post("/sleep")
def sleep(number: str) -> Any:
    pbs_command = ['qsub', '-l', 'nodes=1:ppn=1']
    job_command = ['/bin/sleep', number]
    job_id = ssh_pbs(pbs_command, job_command)
    return job_id
  
  
@router.post("/status")
def get_job_status(job_id: str) -> Any:
    result = job_status(job_id)
    if result:
      return result
    else:
      return Response(status_code=status.HTTP_204_NO_CONTENT)
