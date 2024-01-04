from django.urls import path
from . import views

urlpatterns = [

    path('',views.CustomerListMixin.as_view()),
    path('<int:pk>', views.CustomerDetailMixin.as_view())
]