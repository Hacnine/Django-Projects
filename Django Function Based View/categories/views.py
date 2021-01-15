from django.shortcuts import HttpResponse
from .models import Categories
from django.shortcuts import render


def category_index(request):
    categories = Categories.objects.all()
    return render(request, 'index2.html', {'categories': categories})


def custom(request):
    return HttpResponse('<h1>Custom</h2>')