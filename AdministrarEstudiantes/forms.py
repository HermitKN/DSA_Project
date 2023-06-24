from django import forms

class FormularioEstudiante(forms.Form):

    nombre=forms.CharField(label="Nombre del Estudiante", max_length=20, required=True)
    cedula=forms.CharField(label="C.I. del Estudiante", max_length=20, required=True)
    email=forms.EmailField(label="Correo Electrónico", max_length=20, required=True)
    direccion=forms.CharField(label="Dirección del Estudiante", max_length=50, required=True)
    tfno=forms.CharField(label="Número Telefónico", max_length=20, required=True)