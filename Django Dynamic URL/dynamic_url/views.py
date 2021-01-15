from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render


def home(request, check):
    print(check)
    return render(request, 'home.html')

#
# def show_details(request, my_id):
#     print(my_id)
#     return render(request, 'details.html', {'id': my_id})


def show_details(request, my_id=1):
    employee = {'id': my_id, 'name': 'Tushar'}
    if my_id == 1:
        employee = {'id': my_id, 'name': 'Tushar'}

    elif my_id == 2:
        employee = {'id': my_id, 'name': 'Jahid'}
    # else:
    #     return HttpResponse('<h1>Url not found</h1>')

    return render(request, 'details.html', employee)


def show_sub_details(request, my_id, my_sub_id):
    employee = {'id': my_id, 'name': 'Tushar', 'info': 'Sub Details'}

    if my_id == 1 and my_sub_id == 1:
        employee = {'id': my_id, 'name': 'Tushar', 'info': 'Sub Details'}

    if my_id == 2 and my_sub_id == 2:
        employee = {'id': my_id, 'name': 'Jahid',  'info': 'Sub Details'}

    return render(request, 'sub_detail.html', employee)


def custom_url_converters(request, year):
    # student = {'id': }
    return render(request, 'path_converters.html')
