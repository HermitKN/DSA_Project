from django.shortcuts import render, redirect
from .forms import FormularioLibro
from .models import Libro

# Create your views here.

def administrar_libros(request):
    #Para el Formulario
    FormLibro = FormularioLibro()
    #Para el Listado

    if request.method=="POST":
        FormLibro = FormularioLibro(data=request.POST) 
        if FormLibro.is_valid():
            book = Libro() 
            book.id = FormLibro.cleaned_data['id']
            book.nombre = FormLibro.cleaned_data['nombre']
            book.autor = FormLibro.cleaned_data['autor']
            book.tipo = FormLibro.cleaned_data['tipo']
            book.cantidadint = FormLibro.cleaned_data['cantidadint']
            book.cantidadext = FormLibro.cleaned_data['cantidadext']
            book.descripcion = FormLibro.cleaned_data['descripcion']
            book.categoria = FormLibro.cleaned_data['categoria']
            book.save() 
            return redirect("/administrarlibros/?isvalid")
        
    libros=Libro.objects.all()

    return render(request, "administrarlibros/administrarlibros.html", {'formL':FormLibro, 'libros': libros})

def eliminar_libro(request, id):

    try:
        Libros = Libro.objects.get(id = id)
        Libros.delete()
        Libros = Libro.objects.all()
        FormLibro = FormularioLibro()
        return render(request, "administrarlibros/administrarlibros.html", {'formL':FormLibro, 'libros': Libros})
    except:
        Libros = Libro.objects.all()
        FormLibro = FormularioLibro()
        return render(request, "administrarlibros/administrarlibros.html", {'formL':FormLibro, 'libros': Libros})
    
def editar_libros(request, id):

    try:
        Libros = Libro.objects.get(id = id)
        return render(request, "administrarlibros/editarlibro.html", {'libros': Libros})
    except:
        Libros = Libro.objects.all()
        FormLibro = FormularioLibro()
        return render(request, "administrarlibros/administrarlibros.html", {'formL':FormLibro, 'libros': Libros})
        