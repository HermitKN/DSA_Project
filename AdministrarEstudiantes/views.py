from django.shortcuts import render

# Create your views here.

def administrar_estudiantes(request):

    return render(request, "administrarestudiantes/administrarestudiantes.html")