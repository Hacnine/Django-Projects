from django.shortcuts import render


def serve(request):
    return render(request, 'service_html/services.html')
