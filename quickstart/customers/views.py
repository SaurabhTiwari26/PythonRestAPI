from django.shortcuts import render
from rest_framework import mixins, generics
from .models import Customers
from .customerSerializer import CustomerSerializer

# Create your views here.

class CustomerListMixin(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = Customers.objects.all()
    serializer_class = CustomerSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class CustomerDetailMixin(mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):

    queryset = Customers.objects.all()
    serializer_class = CustomerSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)