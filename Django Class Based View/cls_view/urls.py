from django.urls import path

from . import views

urlpatterns = [
    path('', views.func_view, name='home'),
    path('class/', views.ClassView.as_view(), name='class'),
    # path('class/', views.ClassView.as_view(name='Hujaifa'), name='class'),
    path('class2/', views.ChildClassView.as_view(name='Tarikh'), name='class2'),

    path('contact/', views.contact, name='contact'),
    path('contact-class/', views.ContactClassView.as_view(), name='contact-class'),

    path('template/', views.passing_template, {'template_name': 'passing_template_1.html'}, name='temp'),
    path('templates2/', views.passing_template, {'template_name': 'passing_template_2.html'}, name='templates2'),
    path('templates_class/', views.PassingTemplateView.as_view(), {'template_name': 'passing_template_2.html'}, name='templates_class'),

]
