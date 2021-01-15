from django.core.cache import cache
from django.shortcuts import render


def low_level(request):
    # s1 = cache.get('time', 'has_expired')
    # if s1 == 'has_expired':
    #     cache.set('time', 'Asor', 15)
    #     s1 = cache.get('time')
    #     return render(request, 'low_level.html', {'salah_03': s1})
    salah = cache.get_or_set('salah', 'Asr', 100, version=1)

    # to set many
    data = {'name': 'Tanvir', 'home': 'Damuskandi', 'roll': 100}
    data2 = {'moll': 100}
    # cache.set_many(data, 5)
    # cache.get_many(data)
    # incremnt = cache.incr('moll', delta=2)
    decremnt = cache.decr('roll', delta=1)
    print(decremnt)
    # cache.delete('home', version=2)  # delete will use when you use database
    return render(request, 'low_level.html',{'moll':data2})
