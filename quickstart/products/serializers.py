from rest_framework.serializers import ModelSerializer,SerializerMethodField

from .models import Products


class ProductSerializer(ModelSerializer):
    # sale_price = SerializerMethodField(read_only=True)
    class Meta:
        model = Products
        # fields = ['id','title','content','price']
        fields = ['id', 'title', 'content', 'price', 'sale_price']
        # fields = '__all__'

    def get_sale_price(self,product):
        return float(product.price) * 0.8



class ProductSerializer2(ModelSerializer):
    class Meta:
        model = Products
        fields = ['id']