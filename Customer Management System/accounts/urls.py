from django.contrib.auth import views as auth_views
from django.urls import path

from .views import home, customer, products, create_order, update_order, delete_data, customer_list, login_page, \
    register, user_logout, user_profile, account_settings

urlpatterns = [
    path('', home, name='dashboard'),
    path('login/', login_page, name='login'),
    path('user/', user_profile, name='user-page'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
    path('settings/', account_settings, name='account_settings'),
    path('products/', products, name='products'),
    path('customer/<str:pks>/', customer, name='customer'),
    path('customer_list', customer_list, name='customer_list'),
    path('create_order/<str:pk>/', create_order, name='create_order'),
    path('update_order/<str:order_id>', update_order, name='update_order'),
    path('delete/<int:emp_id>/', delete_data, name='deleted'),
    # path('mash/', search_customer, name='mash')

    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
         name="reset_password"),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"),
         name="password_reset_confirm"),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),
         name="password_reset_complete"),

    # path('update/<int:em_id>/', create_order, name='editupdate'),

]
