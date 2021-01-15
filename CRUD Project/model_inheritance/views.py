from django.shortcuts import render

from .inheritance_form import TeacherRegistration, EmployeeRegistration
from .models import InheritanceUser


def teacher_name(request, id_2):
    if request.method == 'POST':
        form = TeacherRegistration(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TeacherRegistration()
    return render(request, 'inheritance_model.html', {'forms': form})


def employee_name(request,id_1):
    if request.method == 'POST':
        form3 = EmployeeRegistration(request.POST)
        if form3.is_valid():
            form3.save()
    else:
        form3 = EmployeeRegistration()
    return render(request, 'employee_2.html', {'forms2': form3})