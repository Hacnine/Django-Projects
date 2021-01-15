from django.contrib import admin
from contact.models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee_id', 'name', 'email')


# admin.site.register(Employee, EmployeeAdmin)
