from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

# Create your models here.                          1:40hrs
class Destination(models.Model):
    title = models.CharField(max_length=200)
    prod_img = models.ImageField(upload_to='productImg')            #Image Uploader Project
    
    