from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, DetailView
from class_view.models import ClassEmployee


class EmployeeCreateView(CreateView):
    template_name = 'class_employee.html'
    model = ClassEmployee
    fields = ['name', 'email', 'password']

    # success_url = '/name-submit/'


class SubmitTemplateView(TemplateView):
    template_name = 'submit.html'


class EmployeeDetailView(DetailView):
    template_name = 'detail.html'
    model = ClassEmployee
