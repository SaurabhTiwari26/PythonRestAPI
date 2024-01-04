from django.urls import path
from . import views

urlpatterns = [
    # path('',views.products),
    # path('<int:pk>',views.product_detail),
    # path('', views.ProductList.as_view()),
    # path('<int:pk>', views.ProductDetail.as_view()),
    path('', views.ProductListMixin.as_view()),
    path('<int:pk>', views.ProductDetailMixin.as_view()),

]