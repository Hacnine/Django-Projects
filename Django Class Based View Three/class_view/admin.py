from django.contrib import admin
from class_view.models import ClassEmployee


@admin.register(ClassEmployee)
class ClassEmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'password']