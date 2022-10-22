from django.urls import path
from arti.views import login_user, register, logout_user, index

app_name = 'arti'

urlpatterns = [
    path('login', login_user, name='login'),
    path('register', register, name="register"),
    path('logout', logout_user, name="logout"),
    path('', index, name="index"),
]