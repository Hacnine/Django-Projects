from django.contrib import admin

from .models import Categories


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('shirt', 'tShit', 'fruits')


admin.site.register(Categories, CategoriesAdmin)
