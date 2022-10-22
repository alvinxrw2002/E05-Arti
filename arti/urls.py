from django.urls import path
from arti.views import index, login_user, logout_user, register

app_name = 'arti'

urlpatterns = [
    path('', index, name='index'),
    path('login', login_user, name='login'),
    path('register', register, name='register'),
    path('logout', logout_user, name='logout'),
]