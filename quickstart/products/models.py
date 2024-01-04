from django.db import models

# Create your models here.

class Products(models.Model):
    title = models.CharField(default="",max_length=120)
    content = models.TextField(default="")
    price = models.DecimalField(max_digits=15,decimal_places=2,default=99.99)
