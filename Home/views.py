from django.shortcuts import render

# Create your views here.
 
def home(request):

    return render(request, "home/home.html")

def notas_prestamo(request):

    return render(request, "notasprestamo/notasprestamo.html")

def administrar_libros(request):

    return render(request, "administrarlibros/administrarlibros.html")

def administrar_estudiantes(request):

    return render(request, "administrarestudiantes/administrarestudiantes.html")