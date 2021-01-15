from django import forms

from .models import User

password = forms.CharField(max_length=3, required=False)


class UserRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        labels = {'name': 'Enter Your name', 'email': 'Enter your email'}
        help_text = {'name': 'Enter your full name'}
        error_messages = {'name': {'required': 'Name is required'}, 'email': {'required': 'Email is required'} ,
                          'password': {'required': 'Password is required.'}}
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Email Address'}),
            'password': forms.PasswordInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter at least 5 passwords.'}),

        }
