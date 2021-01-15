from django.urls import path

from . import views

urlpatterns = [
    path('', views.category_index),
    path('custom/', views.custom)
]
