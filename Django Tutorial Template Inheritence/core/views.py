from django.shortcuts import render


def home(request):
    return render(request, 'core/home.html', {'django': 'Django'})


def about(request):
    return render(request, 'core/about.html')
    # return render(request, 'core/about.html', {'abc': '/about'})