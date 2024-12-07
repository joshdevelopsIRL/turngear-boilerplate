from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .decorators import auth_required


def user_login(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        creds = {
            "username": request.POST["username"],
            "password": request.POST["password"],
        }
        user = authenticate(request, **creds)
        if user is not None:
            login(request, user)
            messages.success(request, 'User logged in successfully.')
            return redirect('direct')
        messages.warning(request, 'Login failed, please try again.')
        return redirect('login')

    if request.user.is_authenticated:
        return redirect('direct')

    return render(request, 'users/login.html', {})


def user_logout(request: HttpRequest) -> HttpResponse:
    logout(request)
    messages.success(request, 'User logged out successfully.')
    return redirect('login')


@auth_required
def test_login(request: HttpRequest) -> HttpResponse:
    return render(request, 'users/direct.html', {})
