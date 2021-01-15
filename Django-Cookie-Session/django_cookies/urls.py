from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('set/', views.set_cookies, name='set'),
    path('get/', views.get_cookies, name='get'),
    path('del/', views.del_cookies, name='del')
]
