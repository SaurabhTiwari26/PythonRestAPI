from django.http import JsonResponse, Http404
from .models import Products
from .serializers import ProductSerializer, ProductSerializer2

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import mixins, generics

import json


# @api_view(['GET', 'POST'])
# def products(request):
#     if request.method == 'GET':
#         products = Products.objects.all() # return a queryset -> complex data type, convert this to Python's native
#         serialized = ProductSerializer(products, many=True)
#         return Response(serialized.data)
#     elif request.method == 'POST':
#         requestdata = json.loads(request.body)
#         serialized = ProductSerializer(data=requestdata)
#         if serialized.is_valid():
#             serialized.save()
#             return Response(serialized.data, status=201)
#         return Response(serialized.errors, status=400)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def product_detail(request, pk):
#     try:
#         product = Products.objects.get(id=pk)
#     except Products.DoesNotExist:
#         return Response({"detail": "Product not found"}, status=404)
#     if request.method == 'GET':
#         serialized = ProductSerializer(product)
#         return Response(serialized.data)
#     elif request.method == 'PUT':
#         requestdata = json.loads(request.body)
#         serialized = ProductSerializer(product, data=requestdata)
#         if serialized.is_valid():
#             serialized.save()
#             return Response(serialized.data)
#     elif request.method == 'DELETE':
#         product.delete()
#         return Response({'details': 'product deleted successfully'})
#

# class ProductList(APIView):
#
#     def get(self, request):
#         products = Products.objects.all()  # return a queryset -> complex data type, convert this to Python's native
#         serialized = ProductSerializer(products, many=True)
#         return Response(serialized.data)
#
#     def post(self, request):
#         requestdata = json.loads(request.body)
#         serialized = ProductSerializer(data=requestdata)
#         if serialized.is_valid():
#             serialized.save()
#             return Response(serialized.data, status=201)
#         return Response(serialized.errors, status=400)
#
#
# class ProductDetail(APIView):
#
#     def get_product(self, pk):
#         try:
#             return Products.objects.get(id=pk)
#         except Products.DoesNotExist:
#             raise Http404
#             # return Response({"detail": "Product not found"}, status=404)
#
#     def get(self, request, pk):
#         serialized = ProductSerializer(self.get_product(pk))
#         return Response(serialized.data)
#
#     def put(self, request, pk):
#         requestdata = json.loads(request.body)
#         serialized = ProductSerializer(self.get_product(pk), data=requestdata)
#         if serialized.is_valid():
#             serialized.save()
#             return Response(serialized.data)
#
#     def delete(self, request, pk):
#         self.get_product(pk).delete()
#         return Response({'details': 'product deleted successfully'})
#

class ProductListMixin(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = Products.objects.all()
    serializer_class = ProductSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class ProductDetailMixin(mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):

    queryset = Products.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ProductCreateOnly(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

