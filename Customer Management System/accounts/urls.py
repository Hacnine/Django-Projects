from django.http import HttpResponse
from django.urls import path

from .views import home, customer, products


urlpatterns = [
    path('', home, name='dashboard'),
    path('products/', products, name='products'),
    path('customer/', customer, name='customer'),
]
