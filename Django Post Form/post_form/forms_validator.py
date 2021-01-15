from django import forms
from django.core import validators


def starts_with_t(value):
    if value[0] != 'T':
        raise forms.ValidationError('Name should be starts with T')


class FormValidator(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()  # by default strip is True
    password = forms.CharField()
    # # password mathcing
    # password = forms.CharField(widget=forms.PasswordInput, validators=[validators.MinLengthValidator(3)])
    # reenter_password = forms.CharField(widget=forms.PasswordInput)
    #
    # # password mathcing
    # def clean(self):
    #     cleaned_data = super(FormValidator, self).clean()
    #     val_password = self.cleaned_data['password']
    #     val_enterpassword = self.cleaned_data['reenter_password']
    #     if val_password != val_enterpassword:
    #         raise forms.ValidationError('Password not matched')


    # # validation for all fileds
    # def clean(self):
    #     cleaned_data = super(FormValidator, self).clean()
    #     val_name = self.cleaned_data['name']
    #     if len(val_name) < 4:
    #         raise forms.ValidationError('Enter more than or equal four  char')
    #
    #     val_pass = self.cleaned_data['password']
    #     if len(val_pass) < 5:
    #         raise forms.ValidationError('Enter more five password')


    # custom validation message for specific field
    # def clean_name(self):
    #     val_name = self.cleaned_data['name']
    #     if len(val_name) < 3:
    #         # pass
    #         raise forms.ValidationError('Enter more than or equal 3  ')
    #
    #     return val_name
    #
    # def clean_password(self):
    #     val_pass = self.cleaned_data['password']
    #     if len(val_pass) < 2:
    #
    #         raise forms.ValidationError('Enter more 3 password')
    #
    #     return val_pass







