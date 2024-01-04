from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView

from . models import Order
from . OrderSerializers import OrderSerializer
from rest_framework import mixins, generics
import json


# Create your views here.

class OrderDetail(APIView):

    def get_Order(self, pk):
        try:
            return Order.objects.get(id=pk)
        except Order.DoesNotExist:
            raise Http404
            # return Response({"detail": "Product not found"}, status=404)

    def get(self, request, pk):
        serialized = OrderSerializer(self.get_Order(pk))
        return Response(serialized.data)

    def put(self, request, pk):
        requestdata = json.loads(request.body)
        print(requestdata)
        serialized = OrderSerializer(self.get_Order(pk), data=requestdata)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data)

    def delete(self, request, pk):
        Order.objects.all().filter(id=pk).update(is_available="False")
        return Response({'details': 'order deleted successfully'})

class OrderListMixin(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = Order.objects.all().filter(is_available="True")
    serializer_class = OrderSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class OrderDetailMixin(mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):

        return self.destroy(request, *args, **kwargs)