from django.shortcuts import render

# Create your views here.
 
def home(request):

    return render(request, "home/home.html")

def estudiantes(request):

    return render(request, "templates/administrarlibros.html")

def prestamos(request):

    return render(request, "home/home.html")

def notas(request):

    return render(request, "home/home.html")

def libros(request):

    return render(request, "home/home.html")