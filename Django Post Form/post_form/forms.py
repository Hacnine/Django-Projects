from django import forms
from django.core import validators
from django.forms import NullBooleanField, Select


class PostForm(forms.Form):
    # this for form field

    name = forms.CharField(min_length=4, strip=False)
    email = forms.EmailField()  # by default strip is True
    password = forms.CharField(widget=forms.PasswordInput)
    rate = forms.FloatField(min_value=4, max_value=40)
    price = forms.DecimalField(min_value=4, max_value=40, max_digits=4, decimal_places=1)
    agree = forms.BooleanField(label_suffix=' ', label='I Agree')
    agree2 = NullBooleanField(
        widget=Select(
            choices=[
                ('', 'Unknown'),
                (True, 'Yes'),
                (False, 'No'),
            ]
        )
    )
