from datetime import datetime, timedelta

from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def set_cookies(request):
    response = render(request, 'set_cookie.html')
    # response.set_cookie('name', 'Jundullah', expires=datetime.now() + timedelta(days=2))
    response.set_signed_cookie('name', 'Jundullah', salt='nmm', expires=datetime.now() + timedelta(days=2))

    # response.set_cookie('name', 'Jundullah', max_age=60)
    return response


def get_cookies(request):
    # name = request.COOKIES['name']
    # name = request.COOKIES.get('name', "Guest")
    name = request.get_signed_cookie('name', default='Salt value is not matched.Please check salt value.', salt='nm')
    return render(request, 'get_cookie.html', {'name': name})


def del_cookies(request):
    response = render(request, 'del_cookie.html')
    response.delete_cookie('name')
    return response
