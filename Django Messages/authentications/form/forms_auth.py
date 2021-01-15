from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from authentications.models import Blog


class SignUpForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password (again)')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email': 'Email'}


class PostForm(forms.ModelForm):
    class Blog:
        model = User
        fields = '__all__'


class EditUserProfileForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email'] #  you can also add , 'date_joined', 'last_login'
        labels = {'email': 'Email'}


class EditAdminProfileForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = '__all__'
        labels = {'email': 'Email'}