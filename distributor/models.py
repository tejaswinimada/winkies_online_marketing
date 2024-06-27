from django.db import models
from ss.models import *
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class Admin(models.Model):
    username = models.CharField(max_length = 100,default = None)
    password = models.CharField(max_length = 100)
    email = models.EmailField(default = None)


    def __str__(self) -> str:
        return self.first_name
class Requirements(models.Model):
    item_name=models.CharField(max_length=100)
    quantity=models.IntegerField()
    price=models.IntegerField()
    def __str__(self) -> str:
        return self.item_name