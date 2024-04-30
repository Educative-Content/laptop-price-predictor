from django import forms
from .models import Laptop

class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        exclude = ['Price']  # Exclude Price field as it will be predicted
