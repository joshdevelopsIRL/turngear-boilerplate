from django.http import HttpRequest
from django.shortcuts import redirect
from django.contrib import messages


def auth_required(f):
    def wrapper(request: HttpRequest, *args, **kwargs):
        if request.user and request.user.is_authenticated:
            return f(request, *args, **kwargs)
        messages.warning(request, 'User must be logged in.')
        return redirect('login')
    return wrapper
