from django.db import models
from django.contrib.auth.models import User
from arti.models import Karya
# Create your models here.
class Transaksi(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE) 
    karya = models.ForeignKey(Karya,on_delete= models.CASCADE)