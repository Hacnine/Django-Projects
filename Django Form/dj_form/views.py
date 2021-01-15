from django.shortcuts import render
from .forms import EmployeeRegistration
from . models import Employee
from .forms import EmployeeForm, FormFieldArgument


def databases(request):
    # stu = Employee.objects.get(pk=3)
    emp = Employee.objects.all()
    form_class = EmployeeForm()
    return render(request, 'databases_html.html', {'employee': form_class})


def show_form_data(request):
    # if I want to replace 'id' tag with some string ex: 'some'
    employee_form = EmployeeRegistration(auto_id='some_%s')

    # to remove 'id' tag
    employee_form = EmployeeRegistration(auto_id=True)

    # to remove id
    employee_form = EmployeeRegistration(auto_id=False)

    # to remove 'id' tag
    employee_form = EmployeeRegistration(auto_id=True)

    # to remove ':'
    employee_form = EmployeeRegistration(auto_id=True, label_suffix=False)

    # to add suffix in place ':'
    employee_form = EmployeeRegistration(auto_id=True, label_suffix='-')

    # to give initial value
    employee_form = EmployeeRegistration(auto_id=True, label_suffix='-', initial={'name': 'Tushar'})

    # to change field order
    employee_form = EmployeeRegistration(field_order=['last_name', 'name', 'email'])

    employee_form = EmployeeRegistration()

    return render(request, 'show_data.html', {'forms': employee_form})


def form_field_view(request):
    # form_filed_argument
    form_field = FormFieldArgument
    return render(request, 'form_filed_argument.html', {'field_argument': form_field})