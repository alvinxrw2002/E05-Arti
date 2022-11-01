from django.urls import path
from .views import jml_donasi, pesanajax
from django.conf import settings
from django.conf.urls.static import static

app_name = 'riwayat'

urlpatterns = [
    path('', jml_donasi, name='jml_donasi'),
    path('pesanajax/', pesanajax, name='pesanajax'),
]