from django.urls import path
from . import views

urlpatterns = [
    path('', views.aggregation, name='aggregation'),
    # path('', views.),
]
