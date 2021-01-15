from django.contrib import admin

from model_form.models import User


@admin.register(User)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
