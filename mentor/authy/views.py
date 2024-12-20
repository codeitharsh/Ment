from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash, authenticate, login
from django.db.models import Sum
from django.db import transaction
from django.http import HttpResponse
from django.urls import reverse
from django.core.paginator import Paginator
from authy.forms import SignupForm, ChangePasswordForm, EditProfileForm
from authy.models import Profile


def side_nav_info(request):
    """Provide navigation profile information."""
    nav_profile = None
    if request.user.is_authenticated:
        nav_profile = get_object_or_404(Profile, user=request.user)
    return {'nav_profile': nav_profile}


def user_profile(request, username):
    """Display user profile."""
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)
    return render(request, 'profile.html', {'profile': profile})


def signup(request):
    """User signup view."""
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data.get('username'),
                email=form.cleaned_data.get('email'),
                password=form.cleaned_data.get('password'),
            )
            login(request, user)
            return redirect('edit-profile')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def password_change(request):
    """Allow users to change their password."""
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST, instance=request.user)
        if form.is_valid():
            request.user.set_password(form.cleaned_data.get('new_password'))
            request.user.save()
            update_session_auth_hash(request, request.user)
            return redirect('change_password_done')
    else:
        form = ChangePasswordForm(instance=request.user)
    return render(request, 'registration/change_password.html', {'form': form})


def password_change_done(request):
    """Password change confirmation."""
    return render(request, 'change_password_done.html')


@login_required
def edit_profile(request):
    """Edit user profile."""
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EditProfileForm(instance=profile)
    return render(request, 'registration/edit_profile.html', {'form': form})
