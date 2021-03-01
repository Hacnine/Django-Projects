from django.contrib import admin

from accounts.models import *

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)

# from .models import Page
#
#
# @admin.register(Page)
# class PageAdmin(admin.ModelAdmin):
#     list_display = ['page_name', 'page_cat', 'page_publish_date', 'user']