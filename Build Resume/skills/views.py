from django.shortcuts import render


def skills(request):
    return render(request, 'skills_html.html')
