from django.shortcuts import render


def home(request):
    return render(request, 'dashboard.html')


def products(request):
    all_product =
    return render(request, 'products.html')


def customer(request):
    return render(request, 'customer.html')