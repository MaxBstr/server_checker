import platform
import subprocess

from django.shortcuts import redirect
from django.urls import reverse

from server_checker.celery import app
from servers.models import Server


@app.task
def check_connection() -> None:
    servers = Server.objects.all()
    if not servers:
        print('No servers')
        return

    param = '-n' if platform.system().lower() == 'windows' else '-c'
    for server in servers:
        # Building the command. Ex: "ping -c 1 google.com"
        command = ['ping', param, '1', server.ip]
        status = subprocess.call(command)
        # success: ping returns 0 -> in db status bool=True(1)
        # failed: ping returns != 0 value -> in db status bool=False(0)
        status = True if status == 0 else False
        server.status = status
        server.save()

    # TODO: check
    return redirect(reverse('servers:index'))
