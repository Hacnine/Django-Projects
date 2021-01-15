from django.http import HttpResponse
from django.shortcuts import render

from .models import Product


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html',
                  {'products': products})


def home(request):
    return HttpResponse('<h1>Home Page</h1>')


def mew(request):
    return HttpResponse('<h1>Mew Word 2</h1>')


def math(request):
    return HttpResponse(12 + 13)
