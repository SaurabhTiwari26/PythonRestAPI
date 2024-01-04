from django.db import models

# Create your models here.

class Customers(models.Model):
    name = models.CharField(default="",max_length=120)
    address = models.TextField(default="")
    phoneNumber = models.CharField(default=0000000000,max_length=10)
