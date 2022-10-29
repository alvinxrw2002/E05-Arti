from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Karya(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gambar = models.ImageField(upload_to="images/")
    judul = models.CharField(max_length=255)
    harga = models.CharField(max_length=255)
    deskripsi = models.CharField(max_length=10000)
    tanggal = models.DateField(auto_now_add=True)
