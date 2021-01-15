from django.shortcuts import render
from django.http import HttpResponseRedirect
import sqlite3
from post_form.forms import PostForm
from .form_error import FormError
from .forms_validator import FormValidator
from .models import Employee


def sqlite_method(name, email):
    connection = sqlite3.connect('employee.sqlite3')

    carsor = connection.cursor()

    # carsor.execute("""  CREATE TABLE employee_sub (
    #                         first text,
    #                         email text )""")

    carsor.execute("INSERT INTO employee_sub VALUES (?, ?)", (name, email))
    connection.commit()


def post_form(request):

    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            # agree = form.cleaned_data['agree']

            db1 = Employee(name1=name, email1=email)
            db1.save()

            sqlite_method(name, email)

            print('Name:', name)
            print('Email: ', email)
            # print('Agree', agree)
            print("See in Terminal. It has come form 'POST'")

    else:
        form = PostForm()
        print("See in Terminal. It has come form 'GET'")
    return render(request, 'post_html.html', {'forms': form})


def form_validator(request):

    if request.method == 'POST':
        form = FormValidator(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            print('Name:', name)
            print('Email: ', email)
            print("See in Terminal. It has come form 'POST'")

    else:
        form = FormValidator()
        print("See in Terminal. It has come form 'GET'")
    return render(request, 'validator.html', {'validates': form})


def form_error(request):

    if request.method == 'POST':
        form = FormError(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            print('Name:', name)
            print('Email: ', email)
            print("See in Terminal. It has come form 'POST'")

    else:
        form = FormError()
        print("See in Terminal. It has come form 'GET'")
    return render(request, 'form_error.html', {'error': form})


def summit(request):
    return render(request, 'posted.html')
