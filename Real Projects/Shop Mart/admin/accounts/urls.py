from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    # path('/', cart, name=''),
    # path('/', checkout, name='')
]
