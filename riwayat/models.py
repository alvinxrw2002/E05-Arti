from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pesan(models.Model):
    nama = models.CharField(max_length=15)
    isi = models.TextField(max_length=150)

    def __str__(self):
        return self.nama

class Program(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_donasi = models.IntegerField(null=True)
    # name   = models.CharField(max_length=200)
    # donatur = models.ManyToManyField(Donasi, blank=True)

# class Update(models.Model):
#     donatur = models.ManyToManyField(DonasiAPD, blank=True)