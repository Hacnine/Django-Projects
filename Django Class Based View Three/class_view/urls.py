from django.urls import path

from .views import EmployeeCreateView, SubmitTemplateView, EmployeeDetailView

urlpatterns = [
    path('class/', EmployeeCreateView.as_view(), name='class'),
    path('submit/', SubmitTemplateView.as_view(), name='name-submit'),
    path('detail/<int:pk>', EmployeeDetailView.as_view(), name='detail'),

    # path('', views.),
    # path('', views.),
]
