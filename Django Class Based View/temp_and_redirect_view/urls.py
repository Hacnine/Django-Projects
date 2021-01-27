from django.urls import path, include

from temp_and_redirect_view import views

urlpatterns = [
    # path('', views.TemplateView.as_view(template_name='temp_home.html'), name='temp'),
    # path('', views.HomeTemplateView.as_view(), name='temp'),
    # path('', views.HomeTemplateView.as_view(extra_context={'course': 'Python'}), name='temp'),
    path('<int:age>/', views.HomeTemplateView.as_view(extra_context={'course': 'Python'}), name='temp'),

    path('redirects/', views.RedirectView.as_view(url='/temp/23/'), name='redirects'),
    path('red/', views.RedirectView.as_view(url='/temp/23/'), name='redirects'),

    path('google/', views.RedirectView.as_view(url='https://www.google.com'), name='redirects'),
    path('google-cls/', views.GoogleRedirectView.as_view(url='https://www.google.com'), name='redirects'),

    path('red-pat/', views.RedirectView.as_view(pattern_name='temp')),

]
