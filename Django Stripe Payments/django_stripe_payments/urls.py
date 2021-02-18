from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('charge/', views.charge, name="charge"),
    path('success/<str:args>/', views.success_msg, name="success"),
]
