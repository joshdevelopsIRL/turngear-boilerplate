from django.urls import path

from .views import user_login, user_logout, direct, profile
from .views import hx_direct, hx_profile, hx_openprofilebar, delete

urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),

    path('direct/', direct, name='direct'),
    path('hx_direct/', hx_direct, name='hx_direct'),

    path('profile/', profile, name='profile'),
    path('hx_profile/', hx_profile, name='hx_profile'),
    path('hx_openprofilebar/', hx_openprofilebar, name='hx_openprofilebar'),

    path('delete/', delete, name='delete'),
]
