from django import forms

from .models import User

password = forms.CharField(max_length=3, required=False)


class UserRegistration(forms.ModelForm):
    class Meta:
        model = User
        # Showing all fields manually
        fields = ['name', 'email', 'password']

        # I want to show all fields
        # fields = '__all__'

        # I want to show all fields except password
        # exclude = ['password',]
        labels = {'name': 'Enter Your name', 'email': 'Enter your email'}
        help_text = {'name': 'Enter your full name'}
        error_messages = {'name': {'required': 'Name is required'}, 'email': {'required': 'Email is required'},
                          'password': {'required': 'Password is required.'}}
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Email Address'}),
            'password': forms.PasswordInput(render_value=True,
                                            attrs={'class': 'form-control',
                                                   'placeholder': 'Enter at least 5 passwords.'}),

        }
