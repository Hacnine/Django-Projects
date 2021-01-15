from django.urls import path
from . import views

urlpatterns = [
    path('somecourse', views.django_course, name='courseone'),
    ]
