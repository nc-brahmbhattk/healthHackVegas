from django import forms
from . import models

class CreateDrink(forms.ModelForm):
    """docstring for CreateDrink."""
    class Meta:
        model = models.Drink
        fields = ['flavor','size']
