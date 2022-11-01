from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pesan(models.Model):
    nama = models.CharField(max_length=15)
    isi = models.TextField(max_length=150)

    def __str__(self):
        return self.nama