from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = {'employee_id', 'name', 'email', 'subject'}
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'},),
            'email': forms.TextInput(attrs={'class': 'form-control',  'placeholder': 'Enter your Email name'}),
            'employee_id': forms.TextInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),

        }


class EmployeeRegistration(forms.Form):
    name = forms.CharField(initial='Tushar', help_text='you can enter 20 char', disabled=False)

    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}), disabled=True)

    last_name = forms.CharField(widget=forms.TextInput
                                (attrs={'class': 'form-control text-success', 'placeholder': 'Enter your last name'}))
    #  for hidden field
    key = forms.CharField(widget=forms.HiddenInput())


class FormFieldArgument(forms.Form):
    name = forms.CharField(label='Your Name')
    password = forms.CharField(widget=forms.PasswordInput)
    hidden_input = forms.CharField(widget=forms.HiddenInput)
    phone_number = forms.CharField(label='+990 ')
    home_address = forms.CharField(required=False, initial='Dhaka')
    city = forms.CharField(disabled=True)
    material_status = forms.CharField(help_text='Married or Unmarried')
    comments = forms.CharField(widget=forms.Textarea)
    check_box = forms.CharField(widget=forms.CheckboxInput)
    file_input = forms.CharField(widget=forms.FileInput)

    to_add_class = forms.CharField(widget=forms.TextInput(attrs={'class': 'somecss1', 'id': "id1"}))
