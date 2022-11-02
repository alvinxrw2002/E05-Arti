from django.urls import path
from galeri.views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'galeri'

urlpatterns = [
    path('show_galeri/', show_galeri, name='show_galeri'),
    path('delete-karya/<id>', delete_karya, name='delete_karya'),
    path('json/', get_object_karya_json, name='get_json_karya'),

]