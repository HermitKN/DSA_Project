from django import forms
from .models import Prestamo
from AdministrarLibros.models import Libro
from django.core.exceptions import ValidationError

class FormularioPrestamo(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(FormularioPrestamo, self).__init__(*args, **kwargs)
        self.fields['libro'].queryset = Libro.objects.filter(cantidad__gt=0)
        
    def clean(self):
        cleaned_data = super(FormularioPrestamo, self).clean()
        libro = cleaned_data.get('libro')
        cantidad = cleaned_data.get('cantidad')

        if libro and cantidad:
            if cantidad > libro.cantidad:
                raise ValidationError("La cantidad seleccionada excede la cantidad disponible del libro.")

        return cleaned_data

    class Meta:
        model = Prestamo
        fields = ['estudiante', 'libro', 'cantidad', 'tipo']

