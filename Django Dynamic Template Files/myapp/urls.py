from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("new_html/", views.new_html)
]