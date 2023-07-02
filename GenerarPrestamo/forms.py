from django import forms
from .models import Prestamo
from AdministrarLibros.models import Libro
from AdministrarEstudiantes.models import Estudiante
from django.core.exceptions import ValidationError

class FormularioPrestamo(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(FormularioPrestamo, self).__init__(*args, **kwargs)
        self.fields['libro'].queryset = Libro.objects.exclude(
            cantidadint=0, cantidadext=0
        )
        self.fields['estudiante'].queryset = Estudiante.objects.exclude(estatus='Deshabilitado') 
               
    def clean(self):
        cleaned_data = super(FormularioPrestamo, self).clean()
        libro = cleaned_data.get('libro')
        cantidad = cleaned_data.get('cantidad')
        tipo = cleaned_data.get('tipo')

        if tipo == 'Interno' and libro and cantidad:
            if cantidad > libro.cantidadint:
                raise ValidationError("La cantidad seleccionada excede la cantidad disponible del libro interno.")
            
        if tipo == 'Externo' and libro and cantidad:   
            if cantidad > libro.cantidadext:
                raise ValidationError("La cantidad seleccionada excede la cantidad disponible del libro externo.")
        return cleaned_data

    class Meta:
        model = Prestamo
        fields = ['estudiante', 'libro', 'tipo', 'cantidad']

