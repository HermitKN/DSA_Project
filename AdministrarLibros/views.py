from django.shortcuts import render

# Create your views here.

def administrar_libros(request):

    return render(request, "administrarlibros/administrarlibros.html")