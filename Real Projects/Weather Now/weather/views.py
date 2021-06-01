from django.shortcuts import render
import requests
from .models import City
from .form import CityForm


def city_weather(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=0cae9690544d21d158d36e65e5dabcd4'
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
    form = CityForm()

    weather = []
    city_name = City.objects.all()
    for city in city_name:

        req = requests.get(url.format(city)).json()
        # print(req)
        city_weather = {
            'city': city,
            'temperature': req['main']['temp'],
            'description': req['weather'][0]['description'],
            'icon': req['weather'][0]['icon'],
            # 'pressure': req['main']['pressure']

        }
        weather.append(city_weather)
        print(weather)
    context = {'weathers': weather, 'form': form}
    return render(request, 'weather.html', context)


def cart(request):

    context = {}
    return render(request, 'cart.html', context)


def checkout(request):

    context = {}
    return render(request, 'checkout.html', context)


