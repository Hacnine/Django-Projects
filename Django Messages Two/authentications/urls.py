from django.urls import path
from . import views

urlpatterns = [
    path('', views.sign_up),
    path('login/', views.user_login, name='login'),
    # path('profile/', views.user_profile, name='profile'),
    path('logout/', views.user_logout, name='logout'),
    path('detail/<int:ids>', views.user_details, name='detail'),
    path('changepass/', views.user_change_pass, name='changepass'),
    path('change_profile/', views.user_change_profile, name='change_prof'),
    path('chng_pass_without_old/', views.change_pass_without_old, name='except_old'),

    path('dashboard/', views.user_dashboard, name='dashboard'),

]
