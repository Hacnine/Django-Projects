from django.urls import path

from . import views

urlpatterns = [
    path('', views.model, name='model'),
    # path('', views.),
    # path('', views.),
]
