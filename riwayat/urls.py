from django.urls import path
from .views import riwayat, pesanajax
from django.conf import settings
from django.conf.urls.static import static

app_name = 'riwayat'

urlpatterns = [
    path('', riwayat, name='riwayat'),
    path('pesanajax/', pesanajax, name='pesanajax'),
]