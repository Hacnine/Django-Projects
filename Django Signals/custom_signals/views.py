from django.http import HttpResponse
from django.shortcuts import render

from custom_signals import signals


def home(request):
    signals.notification.send(sender=None, request=request,
                              user=['hsasnie', 'Tushar'])
    return HttpResponse('Its home page')
