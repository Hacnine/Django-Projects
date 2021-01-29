from django.urls import path

from form_view import views

urlpatterns = [
    path('', views.ContactFormView.as_view(), name='contact'),
    path('submitted/', views.SubmitTemplateView.as_view(), name='summit')

]