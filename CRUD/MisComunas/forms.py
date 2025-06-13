from django import forms
from .models import comuna

class ComunaForm(forms.ModelForm):
    class Meta:
        model = comuna
        fields = '__all__'
