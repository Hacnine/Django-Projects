from django.urls import path
from generic_view.views import StudentListView

urlpatterns = [
    path('student/', StudentListView.as_view(), name='student')
]
