from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.urls import reverse

from servers.forms import UserProfileUpdateForm, ServerCreateOrUpdateForm
from servers.models import UserProfile, Server
from servers.serializers import UserProfileSerializer, ServerSerializer


def index(request: HttpRequest):
    if not request.user.is_authenticated:
        return redirect(reverse('servers:register'))

    servers = Server.objects.all()
    # Is at least 1 server exists
    if servers:
        context = ServerSerializer(servers, many=True).data
    else:
        context = {}
    return render(request, 'index.html', context)


# Profile stuff
@login_required
def profile(request: HttpRequest):
    user = get_object_or_404(UserProfile, id=request.user.id)
    context = UserProfileSerializer(user).data
    return render(request, 'profile.html', context)


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
    form = ServerCreateOrUpdateForm(request.POST or None, instance=request.POST)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect(reverse('servers:index'))


# Registration stuff
def register(request):
    return render(request, 'registration.html')
