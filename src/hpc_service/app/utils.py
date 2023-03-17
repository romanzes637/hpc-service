import json
import platform
import subprocess

from hpc_service.app.core.config import settings


def ping(host):
    """Ping pong wirh a host"""
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', host]
    proc = subprocess.run(command)
    return not proc.returncode


def ssh(user, host, command):
    """SSH a command to the host"""
    ssh_command = ['ssh', f'{user}@{host}']
    args = ssh_command + command
    proc = subprocess.run(args=args, capture_output=True)
    return proc
  
  
def ssh_pbs(pbs_command, job_command=None):
    """SSH a pbs command with optional job command"""
    if job_command is not None:
        command = pbs_command + ['--'] + job_command
        proc = ssh(settings.HPC_USER, settings.HPC_HOST, command)
    else:
        proc = ssh(settings.HPC_USER, settings.HPC_HOST, pbs_command)
    return proc
    
    
def job_status(job_id):
  """Return job status info"""
  pbs_command = ['qstat', '-f', '-F', 'json', job_id]
  proc = ssh_pbs(pbs_command)
  if proc.returncode:
    return None
  else:
    status = json.loads(proc.stdout)
    return status
  