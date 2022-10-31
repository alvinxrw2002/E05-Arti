from django.urls import path
from arti.views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'arti'

urlpatterns = [
    path('', index, name='index'),
    path('galeri', galeri, name='galeri'),
    path('login', login_user, name='login'),
    path('register', register, name='register'),
    path('logout', logout_user, name='logout'),
    path('post-karya', post_karya, name='post_karya'),
    path('delete-karya/<karya_id>', delete_karya, name='delete_karya'),
    path('edit-karya/<karya_id>', edit_karya, name='edit_karya'),
]