from django.shortcuts import render, redirect
from .forms import FormularioEstudiante # Importamos el formulario de forms.py
from .models import Estudiante # Importamos la tabla de models.py
# Create your views here.

def administrar_estudiantes(request):
    formulario_estudiantes=FormularioEstudiante() # Almacenas el formulario importado en la variable formulario_estudiantes
    if request.method=="POST": # pregunta que si el request es de tipo post
        formulario_estudiantes=FormularioEstudiante(data=request.POST) # Pasamos la petición al formulario para luego poder hacer las validaciones del lado del servidor
        if formulario_estudiantes.is_valid(): # Si es válido puedes acceder a los datos limpios (es decir, validados) a través de la propiedad cleaned_data
            # y al mismo tiempo guarda la información en la base de datos
            estudiante=Estudiante() # creación del objeto de la clase Estudiante importada de models.py
            estudiante.nombre=formulario_estudiantes.cleaned_data['nombre']
            estudiante.cedula=formulario_estudiantes.cleaned_data['cedula']
            estudiante.email=formulario_estudiantes.cleaned_data['email']
            estudiante.direccion=formulario_estudiantes.cleaned_data['direccion']
            estudiante.tfno=formulario_estudiantes.cleaned_data['tfno']
            estudiante.save() # Método que finalmente guarda la información en la base de datos
            return redirect("/administrarestudiantes/?isvalid") # Al final del if se redirecciona a otra url para confirmar que se ha limpiado y enviado la información a la base de datos
        
    estudiantes=Estudiante.objects.last()
    # Se renderiza la plantilla con todos los campos del formulario creado
    return render(request, "administrarestudiantes/administrarestudiantes.html", {'myFormE':formulario_estudiantes, 'estudiantes': estudiantes})
