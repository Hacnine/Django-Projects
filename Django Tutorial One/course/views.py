from django.http import HttpResponse
from django.shortcuts import render


def course_description(request):
    return HttpResponse("Mellow")