from django.contrib import admin

from .models import Work


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ['work_title', 'work_duration', 'done_by']
