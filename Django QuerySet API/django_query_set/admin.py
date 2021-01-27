from django.contrib import admin
from django_query_set.models import Student, Employee


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city', 'marks', 'pass_date']


@admin.register(Employee)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'employee_id', 'city', 'salary', 'join_date']
