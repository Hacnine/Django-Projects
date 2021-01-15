from django.urls import path

from . import views

urlpatterns = [
    path('page', views.count_page, name='page'),
    path('set/', views.set_session, name='set_session2'),
    path('get/', views.get_session, name='get_session2'),
    path('del/', views.del_session, name='del_session2'),
]
