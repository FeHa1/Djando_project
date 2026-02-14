from django import forms
from .models import Deudor

class DeudorForm(forms.ModelForm):
    class Meta:
        model = Deudor
        fields = ['nombre_completo', 'dni', 'email', 'telefono', 'deuda', 'estado']
