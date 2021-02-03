from django.contrib import admin

from .models import Customer, Order, Product, Tag


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'email', 'date_created']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'description', 'date_created']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'product', 'date_created', 'status']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']

