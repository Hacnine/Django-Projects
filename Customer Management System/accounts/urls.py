from django.urls import path

from .views import home, customer, products, create_order, update_order

urlpatterns = [
    path('', home, name='dashboard'),
    path('products/', products, name='products'),
    path('customer/<str:pks>/', customer, name='customer'),
    path('create_order/', create_order, name='create_order'),
    path('update_order/<str:order_id>', update_order, name='update_order'),

    # path('update/<int:em_id>/', create_order, name='editupdate'),

]
