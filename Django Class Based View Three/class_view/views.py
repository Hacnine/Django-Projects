from django.views.generic import CreateView, TemplateView, DetailView

from class_view.forms import EmployeeForm
from class_view.models import ClassEmployee


# class EmployeeCreateView(CreateView):
#     template_name = 'class_employee.html'
#     form_class = EmployeeForm
# model = ClassEmployee
# fields = ['name', 'email', 'password']
#
# # success_url = '/name-submit/'
#
# def get_form(self):
#     form = super().get_form()
#     form.fields['name'].widget = forms.TextInput(attrs={'class': 'form-control'})
#     form.fields['password'].widget = forms.PasswordInput()
#
#     return form


class EmployeeCreateView(CreateView):
    template_name = 'class_employee.html'
    form_class = EmployeeForm


class SubmitTemplateView(TemplateView):
    template_name = 'submit.html'


class EmployeeDetailView(DetailView):
    template_name = 'detail.html'
    model = ClassEmployee
