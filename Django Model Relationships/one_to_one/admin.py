from django.contrib import admin
from .models import Page, PageThree, Like


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['page_name', 'page_cat', 'page_publish_date', 'user']


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['likes', 'page_name', 'page_cat', 'page_publish_date', 'user']


@admin.register(PageThree)
class PageThreeAdmin(admin.ModelAdmin):
    list_display = ['page_name', 'page_cat', 'page_publish_date', 'muser']
