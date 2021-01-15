from django.urls import path
from . import views
urlpatterns = [
    path('', views.post_form),
    path('validator/', views.form_validator, name='valid'),
    path('posted/', views.summit),
    path('error/', views.form_error, name='error')
]