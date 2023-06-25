from django import forms
from .models import Estudiante

class FormularioEstudiante(forms.Form): #Creación de formulario con el nombre FormularioEstudiante
    # Campos del formulario
    id=forms.CharField(label="C.I. del Estudiante", max_length=20, required=True)
    nombre=forms.CharField(label="Nombre del Estudiante", max_length=20, required=True)
    email=forms.EmailField(label="Correo Electrónico", max_length=50, required=True)
    direccion=forms.CharField(label="Dirección del Estudiante", max_length=50, required=True)
    tfno=forms.CharField(label="Número Telefónico", max_length=20, required=True)

    def clean_id(self):
        id = self.cleaned_data['id']
        if Estudiante.objects.filter(id=id).exists():
            raise forms.ValidationError("La cédula del estudiante ya existe")
        return id