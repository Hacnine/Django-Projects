from django.urls import path, register_converter
from . import views, converters

register_converter(converters.FourDigitConverter, 'yyyy')

urlpatterns = [
    path('', views.add_show, name='addshow'),
    path('update/<int:em_id>/', views.edit_update, name='editupdate'),
    path('', views.redirect_home, name='home'),

    path('delete/<int:emp_id>/', views.delete_data, name='deletedata'),
    # path('/dat/<yyyy:year>/', views.custom_url_converters, name='details'),

]