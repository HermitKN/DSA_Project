from django import forms
from .models import Libro

class FormularioLibro(forms.ModelForm): #Creación de formulario con el nombre FormularioLibro

    class Meta: 
        model = Libro
        fields = ['id','nombre','autor','tipo', 'cantidadint', 'cantidadext', 'descripcion' , 'categoria']

    # Campos del formulario
    #id=forms.CharField(label="Cota", max_length=20, required=True)
    #nombre=forms.CharField(label="Nombre del Libro", max_length=50, required=True)
    #autor=forms.CharField(label="Autor", max_length=50, required=True)
    #tipo=forms.ChoiceField(label="Tipo", choices=Choice_Libro)
    #cantidadint = forms.IntegerField(label="Copias Internas",required=True)
    #cantidadext = forms.IntegerField(label="Copias Externas",required=True)
    #categoria=forms.CharField(label="Tags", max_length=20, required=True)

    def clean_id(self):
        id = self.cleaned_data['id']
        if Libro.objects.filter(id=id).exists():
            raise forms.ValidationError("El ID del libro ya existe")
        return id