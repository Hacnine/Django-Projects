from django import forms
from django.core import validators


class FormError(forms.Form):
    error_css_error = 'error'

    name = forms.CharField(error_messages={'required': 'Enter your name'})
    email = forms.EmailField(error_messages={'required': 'Enter your email'}, min_length=3)

    # Follow the video: Styling Django Form Errors and Field Error in Django (Hindi)
