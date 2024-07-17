from django.db import models
from ss.models import *
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class Admin(models.Model):
    username = models.TextField(max_length = 100,default = None)
    password = models.CharField(max_length = 100)
    email = models.EmailField(default = None)


    def __str__(self) -> str:
        return self.username
# class Items(models.Model):
#     item_name = models.CharField(max_length=50)
#     quantity = models.IntegerField()
#     price = models.DecimalField(max_digits=5, decimal_places=2)
#     is_available = models.BooleanField(default=True)
#     is_new = models.BooleanField(default=True)
    

#     def __str__(self):
#         return self.item_name
class Requirements(models.Model):
    item_name=models.CharField(max_length=100)
    quantity=models.IntegerField()
    price=models.IntegerField()
   
    def __str__(self) -> str:
        return self.item_name