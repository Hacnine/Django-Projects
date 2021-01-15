from django.urls import path, register_converter
from . import views, converters

register_converter(converters.FourDigitYearConverter, 'yyyy')

urlpatterns = [
    path('', views.home, {'check': 'HOME'}, name='home'),
    # path('go/<my_id>/', views.show_details, name='detail'),
    path('go/<int:my_id>/', views.show_details, name='detail'),
    path('go/<int:my_id>/<int:my_sub_id>/', views.show_sub_details, name='sub_details'),
    
    # custom path converters
    path('co/<yyyy:year>/', views.custom_url_converters),

]