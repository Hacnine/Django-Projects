from django.urls import path

from . import views

urlpatterns = [
    path('home', views.home, name='page'),
    # path('', views.),
    # path('', views.),
]
