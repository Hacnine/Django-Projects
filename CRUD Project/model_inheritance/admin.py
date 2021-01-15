from django.contrib import admin
from .models import InheritanceUser


@admin.register(InheritanceUser)
class InheritanceUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'teacher_name', 'employee_name', 'email', 'password')
