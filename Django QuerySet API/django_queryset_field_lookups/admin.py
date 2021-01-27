from django.contrib import admin
from django_queryset_field_lookups.models import StudentTwo


@admin.register(StudentTwo)
class StudentTwoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city', 'marks', 'admission_datetime', ]
