from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

'''class Product(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)

    def __str__(self):
        return self.username'''

'''
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_number = models.IntegerField()
    address = models.CharField(max_length=200)
    pincode = models.IntegerField()
    house_number = models.CharField(max_length=50,default=None)

    def __str__(self):
        return self.user.f_name



class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return str(self.id)
'''