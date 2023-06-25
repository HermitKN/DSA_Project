from django.shortcuts import render, redirect
from .forms import FormularioLibro
from .models import Libro

# Create your views here.

def administrar_libros(request):

    FormLibro = FormularioLibro()

    if request.method=="POST":
        FormLibro = FormularioLibro(data=request.POST) 
        if FormLibro.is_valid():
            book = Libro() 
            book.id = FormLibro.cleaned_data['id']
            book.nombre = FormLibro.cleaned_data['nombre']
            book.autor = FormLibro.cleaned_data['autor']
            book.tipo = FormLibro.cleaned_data['tipo']
            book.cantidad = FormLibro.cleaned_data['cantidad']
            book.categoria = FormLibro.cleaned_data['categoria']
            book.save() 
            return redirect("/administrarlibros/?isvalid")
        
    books=Libro.objects.last()

    return render(request, "administrarlibros/administrarlibros.html", {'formL':FormLibro, 'books': books})