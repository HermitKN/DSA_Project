from django import forms

Choice_Libro = [
    ('Tesis','Tesis'),
    ('Libros','Libro'),
]

class FormularioLibro(forms.Form): #Creación de formulario con el nombre FormularioLibro

    # Campos del formulario
    id=forms.CharField(label="Id", max_length=20, required=True)
    nombre=forms.CharField(label="Nombre del Libro", max_length=50, required=True)
    autor=forms.CharField(label="Autor", max_length=50, required=True)
    tipo=forms.ChoiceField(label="Tipo", choices=Choice_Libro)
    categoria=forms.CharField(label="Tags", max_length=20, required=True)
    cantidad = forms.IntegerField(label="Numero de Copias",required=True)