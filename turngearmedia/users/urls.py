from django.urls import path

from .views import user_login, user_logout, test_login

urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('direct/', test_login, name='direct'),
]
