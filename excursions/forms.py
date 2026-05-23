from django import forms
from .models import Excursion

class ExcursionForm(forms.ModelForm):
    class Meta:
        model = Excursion
        fields = ['title', 'description', 'price', 'date', 'image', 'duration']
