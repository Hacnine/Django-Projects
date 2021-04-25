from django import forms
from .models import City
from django.forms import ModelForm
from django.forms import ModelForm, TextInput



from django import forms
from .models import City


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'
        widgets = {'name': forms.TextInput(attrs={'class': 'input', 'placeholder': 'City Name'}),
        }


