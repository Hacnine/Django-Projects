from django.contrib import admin
from .models import StudentTwo, ExamCenter


@admin.register(StudentTwo)
class StudentTwoAdmin(admin.ModelAdmin):
    list_display = ['id','cname', 'name', 'roll', 'city']


@admin.register(ExamCenter)
class ExamCenterAdmin(admin.ModelAdmin):
    list_display = ['id', 'cname', 'city']
