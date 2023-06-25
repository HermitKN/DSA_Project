from django import forms

class FormularioEstudiante(forms.Form): #Creación de formulario con el nombre FormularioEstudiante
    # Campos del formulario
    id=forms.CharField(label="C.I. del Estudiante", max_length=20, required=True)
    nombre=forms.CharField(label="Nombre del Estudiante", max_length=20, required=True)
    email=forms.EmailField(label="Correo Electrónico", max_length=50, required=True)
    direccion=forms.CharField(label="Dirección del Estudiante", max_length=50, required=True)
    tfno=forms.CharField(label="Número Telefónico", max_length=20, required=True)