from rest_framework.serializers import ModelSerializer
from . models import Order

class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'customer_id','product_name','price', 'quantity','order_date']


