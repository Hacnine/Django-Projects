from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('update_item/', update_item, name='update_item'),
    path('process_order/', process_order, name='process_order'),

]
