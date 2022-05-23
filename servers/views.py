from collections import defaultdict

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import get_user_model, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.urls import reverse

from servers.forms import UserProfileUpdateForm, ServerCreateOrUpdateForm, UserCreateForm
from servers.models import UserProfile, Server


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
    context['form'] = ServerCreateOrUpdateForm()
    return context


def index(request: HttpRequest):
    if not request.user.is_authenticated:
        return redirect(reverse('servers:register'))

    context = load_context()
    return render(request, 'index.html', context={'context': context})


# Profile stuff
@login_required
def profile(request: HttpRequest):
    return render(request, 'profile.html')


@login_required
def edit_profile(request: HttpRequest):
    form = UserProfileUpdateForm(request.POST or None, instance=request.user)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect(reverse('servers:profile'))

    form = UserProfileUpdateForm()
    return render(request, 'edit_profile.html', {'form': form})


# Server stuff
@staff_member_required
def create_or_update_server(request):
    form = ServerCreateOrUpdateForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        server = form.save(commit=False)
        server.status = False
        server.save()
    return redirect(reverse('servers:index'))


# Registration stuff
def register(request):
    if not request.user.is_anonymous:
        return redirect(reverse('servers:index'))

    form = UserCreateForm(request.POST or None, instance=request.POST)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect(reverse('servers:index'))

    return render(request, 'registration.html', {'form': form})


@login_required
def logout_user(request):
    logout(request.user)
    return redirect(reverse('servers:index'))
