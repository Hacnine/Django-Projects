from django.urls import path
from . import views
urlpatterns = [
    path('', views.count_page, name='page'),
]