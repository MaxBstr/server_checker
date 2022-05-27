from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse

from users.forms import UserSignUpForm, UserProfileUpdateForm


def signup(request: HttpRequest):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('servers:index'))
    else:
        form = UserSignUpForm()
    return render(request, 'auth/signup.html', {'form': form})


@login_required
def profile(request: HttpRequest):
    return render(request, 'profile.html')


@login_required
def edit_profile(request: HttpRequest):
    form = UserProfileUpdateForm(request.POST or None, instance=request.user)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect(reverse('users:profile'))

    form = UserProfileUpdateForm()
    return render(request, 'edit_profile.html', {'form': form})
