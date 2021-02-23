from django.contrib import admin
from .models import Course, CourseModule, Profile

admin.site.register(Course)
admin.site.register(CourseModule)
admin.site.register(Profile)

# from .models import Page
#
#
# @admin.register(Page)
# class PageAdmin(admin.ModelAdmin):
#     list_display = ['page_name', 'page_cat', 'page_publish_date', 'user']