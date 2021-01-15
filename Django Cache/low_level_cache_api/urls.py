
from django.urls import path
from . import views

urlpatterns = [
    path('', views.low_level, name='low_level'),
]