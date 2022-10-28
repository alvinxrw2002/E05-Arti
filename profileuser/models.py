from django.db import models

# Create your models here.

class Profile(models.Model):
    username = models.TextField()
    email = models.TextField()
    phone = models.TextField()
    mobile = models.TextField()
    address = models.TextField()
    finish = models.BooleanField(default=False)

class UploadImage(models.Model):  
    image = models.ImageField(upload_to='images')  
   