from django.urls import path

from model_inheritance import views

urlpatterns = [
    path('emp/<str:id_1>/', views.employee_name, name='employee'),
    path('<str:id_2>/', views.teacher_name, name='teacher'),
]
