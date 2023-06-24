from django.shortcuts import render, redirect
from .forms import FormularioEstudiante
from .models import Estudiante
# Create your views here.

def administrar_estudiantes(request):
    formulario_estudiantes=FormularioEstudiante()
    if request.method=="POST":
        formulario_estudiantes=FormularioEstudiante(data=request.POST)
        if formulario_estudiantes.is_valid():
            estudiante=Estudiante()
            estudiante.nombre=formulario_estudiantes.cleaned_data['nombre']
            estudiante.cedula=formulario_estudiantes.cleaned_data['cedula']
            estudiante.email=formulario_estudiantes.cleaned_data['email']
            estudiante.direccion=formulario_estudiantes.cleaned_data['direccion']
            estudiante.tfno=formulario_estudiantes.cleaned_data['tfno']
            estudiante.save()
            return redirect("/administrarestudiantes/?isvalid")
        
    estudiantes=Estudiante.objects.last()
    return render(request, "administrarestudiantes/administrarestudiantes.html", {'myFormE':formulario_estudiantes, 'estudiantes': estudiantes})