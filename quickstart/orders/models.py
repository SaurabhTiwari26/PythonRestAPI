from django.db import models

# Create your models here.


class Order(models.Model):
    customer_id = models.IntegerField(default=-1)
    product_name = models.CharField(default="",max_length=120)
    price = models.CharField(default="1",max_length=120)
    quantity = models.CharField(default="1",max_length=120)
    order_date = models.DateField(default="",max_length=120)
    is_available = models.CharField(default=True,max_length=5)