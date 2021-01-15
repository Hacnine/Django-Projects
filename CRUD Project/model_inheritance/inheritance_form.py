from django import forms

from .models import InheritanceUser


class TeacherRegistration(forms.ModelForm):
    class Meta:
        model = InheritanceUser
        # fields = ['teacher_name', 'email', 'password']
        exclude = ['employee_name', ]


class EmployeeRegistration(TeacherRegistration):
    class Meta(TeacherRegistration.Meta):
        exclude = ['teacher_name', ]
        labels = {'employee_name': 'Enter Your name', 'email': 'Enter your email'}

