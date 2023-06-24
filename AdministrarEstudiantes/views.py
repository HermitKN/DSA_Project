from django.shortcuts import render, redirect
from .forms import FormularioEstudiante # Importamos el formulario de forms.py
from .models import Estudiante # Importamos la tabla de models.py
# Create your views here.

def administrar_estudiantes(request):
    formulario_estudiantes=FormularioEstudiante() # Almacenas el formulario importado en la variable formulario_estudiantes
    if request.method=="POST":
        formulario_estudiantes=FormularioEstudiante(data=request.POST)
        if formulario_estudiantes.is_valid(): # Si es válido, puedes acceder a los datos limpios (es decir, validados) a través de la propiedad cleaned_data
            # Guardar la información en la base de datos
            estudiante=Estudiante()
            estudiante.nombre=formulario_estudiantes.cleaned_data['nombre']
            estudiante.cedula=formulario_estudiantes.cleaned_data['cedula']
            estudiante.email=formulario_estudiantes.cleaned_data['email']
            estudiante.direccion=formulario_estudiantes.cleaned_data['direccion']
            estudiante.tfno=formulario_estudiantes.cleaned_data['tfno']
            estudiante.save()
            return redirect("/administrarestudiantes/?isvalid")
        
    estudiantes=Estudiante.objects.last()
    # Se renderiza la plantilla con todos los campos del formulario creado
    return render(request, "administrarestudiantes/administrarestudiantes.html", {'myFormE':formulario_estudiantes, 'estudiantes': estudiantes})
