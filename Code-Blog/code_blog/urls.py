from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.user_dashboard, name='dashboard'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('addpost/', views.add_post, name='addpost'),
    path('update/<int:ids>/', views.update_post, name='update'),
    path('delete/<int:ids>/', views.delete_post, name='delete'),
]