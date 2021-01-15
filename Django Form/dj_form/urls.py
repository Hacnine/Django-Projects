from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.show_form_data),
    path('database/', views.databases),
    path('form-field/', views.form_field_view)
]
