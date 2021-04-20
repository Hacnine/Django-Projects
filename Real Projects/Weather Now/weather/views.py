from datetime import datetime, timedelta
import stripe
from django.shortcuts import render, redirect


def city_weather(request):
    context = {}
    return render(request, 'weather.html', context)


def cart(request):

    context = {}
    return render(request, 'cart.html', context)


def checkout(request):

    context = {}
    return render(request, 'checkout.html', context)


