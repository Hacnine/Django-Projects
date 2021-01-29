from django.urls import path
from list_view.views import StudentListView

urlpatterns = [
    path('student/', StudentListView.as_view(), name='student')
]
