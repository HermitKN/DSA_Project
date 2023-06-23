from django import forms

class FormularioPrestamo(forms.Form):

    cedula=forms.CharField(label="C.I. del Estudiante", required=True)
    codigo=forms.CharField(label="Código del Libro", required=True)
    limite=forms.DateField(label="Fecha límite de entrega", required=True)
