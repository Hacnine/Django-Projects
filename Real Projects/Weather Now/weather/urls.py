from django.urls import path

from . import views

urlpatterns = [
    path('', views.city_weather, name='city_weather'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout')
]
