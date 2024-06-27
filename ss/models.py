from django.db import models
from django.contrib.auth.models import User



    
class Stockist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()
    phonenumber = models.IntegerField()
    

    def __str__(self) -> str:
        return self.first_name

class Items(models.Model):
    item_name = models.CharField(max_length = 50)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits = 5,decimal_places=2)
    is_available = models.BooleanField(default=True)
    is_new = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.item_name
class Distributor(models.Model):
    name = models.CharField(max_length = 50)
    area= models.TextField()
    phonenumber = models.IntegerField()
    def __str__(self) -> str:
        return self.name
class Orders(models.Model):
    item_name=models.CharField(max_length=100)
    quantity = models.IntegerField()
    price=models.DecimalField(max_digits=5,decimal_places=2)
    def __str__(self) -> str:
        return self.item_name
            


