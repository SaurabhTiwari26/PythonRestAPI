from rest_framework.serializers import ModelSerializer,SerializerMethodField

from .models import Customers

class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customers
        fields = ['id', 'name', 'address', 'phoneNumber']
