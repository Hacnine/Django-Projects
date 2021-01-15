from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path('filter', views.using_filters),
    path('date-time', views.times_dates),
    path('if', views.if_learn),
    path('for', views.for_loop),
    path('for2', views.for_predefined),
    path('js', views.javascripts)
]