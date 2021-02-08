from django.urls import path

from .views import home, customer, products, create_order, update_order, delete_data, customer_list, login_page, \
    register, user_logout

urlpatterns = [
    path('', home, name='dashboard'),
    path('login/', login_page, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
    path('products/', products, name='products'),
    path('customer/<str:pks>/', customer, name='customer'),
    path('customer_list', customer_list, name='customer_list'),
    path('create_order/<str:pk>/', create_order, name='create_order'),
    path('update_order/<str:order_id>', update_order, name='update_order'),
    path('delete/<int:emp_id>/', delete_data, name='deleted'),
    # path('mash/', search_customer, name='mash')

    # path('update/<int:em_id>/', create_order, name='editupdate'),

]
