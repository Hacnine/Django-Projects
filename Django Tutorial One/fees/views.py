from django.http import HttpResponse
from django.shortcuts import render


def fees_description(request):
    return HttpResponse('Mellow Fees')
