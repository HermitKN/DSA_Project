from django import forms

class FormularioPrestamo(forms.Form):

    nota=forms.IntegerField(label="Nota del Prestamo", required=True)
    cedula=forms.CharField(label="C.I. del Estudiante", required=True)
    codigo=forms.CharField(label="Código del Libro", required=True)
    #fecha=forms.DateField(label="Fecha del Prestamo", auto_now_add=True)
    limite=forms.DateField(label="Fecha límite de entrega", required=True)
