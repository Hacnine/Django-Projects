from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    a = 10 / 0
    return HttpResponse('10 can not dived by 0')
