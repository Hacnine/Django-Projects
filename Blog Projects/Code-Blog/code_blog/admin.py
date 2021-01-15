from django.contrib import admin

from code_blog.models import Post


@admin.register(Post)
class BlogModel(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'body']

