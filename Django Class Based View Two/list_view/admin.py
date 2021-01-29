from django.contrib import admin

from list_view.models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'course']

