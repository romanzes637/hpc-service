import platform
import subprocess


def ping(host):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', host]
    proc = subprocess.run(command)
    return not proc.returncode
