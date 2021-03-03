from datetime import datetime, timedelta
import stripe
import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import *


def store(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cart_items = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0, 'shipping': False}
        cart_items = order['get_cart_items']

    products = Product.objects.all()
    context = {'products': products, 'cart_items': cart_items}
    print('cart_items', cart_items)
    return render(request, 'store.html', context)


def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cart_items = order.get_cart_items

    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0, 'shipping': False}
        cart_items = order['get_cart_items']

    context = {'items': items, 'order': order, 'cart_items': cart_items}
    return render(request, 'cart.html', context)


from django.views.decorators.csrf import csrf_exempt


# @csrf_exempt
def checkout(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cart_items = order.get_cart_items

    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0, 'shipping': False}
        cart_items = order['get_cart_items']

    context = {'items': items, 'order': order, 'cart_items': cart_items}
    return render(request, 'checkout.html', context)


def update_item(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('productId', productId)
    print('action', action)

    customer = request.user.customer
    product = Product.objects.get(id=productId)

    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = orderItem.quantity + 1
    elif action == 'remove':
        orderItem.quantity = orderItem.quantity - 1

    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('It was added', safe=False)


