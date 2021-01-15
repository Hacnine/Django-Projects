from django.shortcuts import render
from datetime import datetime


def home(request):
    return render(request, 'myapplication/home.html')


# using filters
def using_filters(request):
    string1 = {'nm': 'Django is  little complicated.'}
    # string1 = {'': ''} it for default filter
    return render(request, 'filter_template/filters_html.html', string1)


def times_dates(request):
    current_time = datetime.now()
    return render(request, 'date_time_template/date_and_time.html', {'c_time': current_time})


# if condition
def if_learn(request):
    Bool = True
    string = "Django"
    return render(request, 'if_html/if_condition.html', {'check': Bool, 'string': string})


# for loop
def for_loop(request):
    student = {'names': ['Rasel', 'Sohan', 'Nitun']}
    return render(request, 'for_html/for_loop.html', student)
    # Basic for loop
    # return render(request, 'for_html/for_loop.html')


# predefined for loop
def for_predefined(request):
    stu = {'stu1': {'name': 'rahul', 'roll': 101},
           'stu2': {'name': 'Tanvir', 'roll': 102}
           }
    data = {'name': 'Kalam', 'roll': 105}
    student2 = {'student': stu}
    return render(request, 'for_html/for_loop_2.html', student2)

    # return render(request, 'for_html/for_loop_2.html', {'data': data})


def javascripts(request):
    return render(request, 'js_html/js_file.html')

