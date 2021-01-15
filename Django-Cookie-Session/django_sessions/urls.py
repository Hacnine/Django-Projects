from django.urls import path

from . import views

urlpatterns = [
    path('set/', views.set_session, name='set_session'),
    path('get/', views.get_session, name='get_session'),
    path('del/', views.del_session, name='del_session'),
    path('set_test_cookie/', views.set_test_cookie, name='set_test_cookie'),
    path('check_test_cookie/', views.check_test_cookie, name='check_test_cookie'),
    path('del_test_cookie/', views.del_test_cookie, name='del_test_cookie'),

]
