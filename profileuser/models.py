from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    username = models.TextField()
    email = models.TextField()
    phone = models.TextField()
    mobile = models.TextField()
    address = models.TextField()
    finish = models.BooleanField(default=False)

class UploadImage(models.Model): 
    image = models.ImageField(upload_to='images')  
   