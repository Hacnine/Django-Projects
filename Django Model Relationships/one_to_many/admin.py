from django.contrib import admin

from .models import PostTwo


@admin.register(PostTwo)
class PostAdmin(admin.ModelAdmin):
    list_display = ['post_title', 'page_category', 'page_publish_date', 'user']
