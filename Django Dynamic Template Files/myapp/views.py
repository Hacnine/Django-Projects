from django.shortcuts import render


def home(request):
    duration = '4 month'
    seats = 5
    # context_name = {'cname': 'Django', 'du': duration, 'st': seats}
    # return render(request, 'myapplication/home.html', context=context_name)
    # return render(request, 'myapplication/home.html', context_name)
    return render(request, 'myapplication/home.html', {'cname': 'Django', 'du': duration, 'st': seats})



def new_html(request):
    return render(request, 'myapplication/new_html.html')