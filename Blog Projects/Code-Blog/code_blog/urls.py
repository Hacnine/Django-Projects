from django.urls import path, include
from .views import HomeView, ArticleDetailView, ProfileView

urlpatterns = [

    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
