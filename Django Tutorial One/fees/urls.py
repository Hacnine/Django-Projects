from django.urls import path
from . import views


urlpatterns = [
    path('fees/', views.fees_description),
    path('whateverIwant/', views.fees_description),
]