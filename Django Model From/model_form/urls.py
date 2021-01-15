from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.f_model),
    ]
# {% url 'error' %}