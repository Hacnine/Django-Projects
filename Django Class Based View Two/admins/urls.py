"""admins URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from detail_view import views
from detail_view.views import StudentDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('list_view.urls')),
    # path('detail/<int:pk>/', views.StudentDetailView.as_view(), name='detail')
    path('detail/<int:idd>/', views.StudentDetailView.as_view(), name='detail'),
    path('student2/', views.StudentLstView.as_view(), name='student'),

    path('contact/', include('form_view.urls'))
]
