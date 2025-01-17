from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.TextChoices):
    COMPUITERS = 'Computers'
    FOOD = 'Food'
    KIDS = 'Kids'
    HOME = 'Home'

class Product(models.Model):
    name = models.CharField(max_length=200,default='',blank=False)
    desc = models.TextField(max_length=1000,default="",blank=False)
    price = models.DecimalField(max_digits=7,decimal_places=2,default=0)
    brand = models.CharField(max_length=200,default="", blank=False)
    category = models.CharField(max_length=40,choices=Category.choices)
    ratings = models.DecimalField(max_digits=3,decimal_places=2,default=0)
    stock = models.BigIntegerField(default=0)
    creatAt = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.name