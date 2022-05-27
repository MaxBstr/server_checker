from collections import defaultdict

from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.urls import reverse

from servers.forms import ServerCreateOrUpdateForm
from servers.models import Server


def load_context():
    servers = Server.objects.all()
    context = defaultdict()
    context['servers'] = []
    # Is at least 1 server exists
    if servers:
        for server in servers:
            server_data = {
                'ip': server.ip,
                'name': server.name,
                'status': server.status
            }
            context['servers'].append(server_data)
    return context


def index(request: HttpRequest):
    if not request.user.is_authenticated:
        return redirect(reverse('users:login'))

    context = load_context()
    return render(request, 'index.html', context={'context': context})


@staff_member_required
def add_server(request):
    form = ServerCreateOrUpdateForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        server = form.save(commit=False)
        server.status = False
        server.save()
        return redirect(reverse('servers:index'))

    form = ServerCreateOrUpdateForm()
    return render(request, 'add_server_page.html', {'form': form})
