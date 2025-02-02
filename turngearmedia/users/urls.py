from django.urls import path

from .views import user_login, user_logout, direct, profile
from .views import hx_direct, hx_profile, hx_openprofilebar, delete

urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('direct/', direct, name='direct'),
    path('profile/', profile, name='profile'),
]
