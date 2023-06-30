from django import forms
from .models import Prestamo

class FormularioPrestamo(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ['estudiante', 'libro', 'tipo']

