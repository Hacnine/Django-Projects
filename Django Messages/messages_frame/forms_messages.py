from django import forms
from .models import User


class UserRegistration(forms.ModelForm):
    class Meta(User):
        model = User
        fields = '__all__'
        # exclude = ['password',]
