from django.urls import path
from . import views

urlpatterns = [
    path('',views.OrderListMixin.as_view()),
    # path('<int:pk>',views.OrderDetailMixin.as_view())
    path('<int:pk>',views.OrderDetail.as_view())
]