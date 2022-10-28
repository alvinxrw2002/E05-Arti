from django.urls import path
from arti.views import index, login_user, logout_user, register, post_karya
from django.conf import settings
from django.conf.urls.static import static

app_name = 'arti'

urlpatterns = [
    path('', index, name='index'), # Ini halaman utamanya, gess
    path('login', login_user, name='login'),
    path('register', register, name='register'),
    path('logout', logout_user, name='logout'),
    path('post-karya', post_karya, name='post_karya'),
]