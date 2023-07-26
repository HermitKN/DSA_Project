from django.shortcuts import render, redirect
from .forms import FormularioEstudiante 
from .models import Estudiante 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
# Create your views here.

def administrar_estudiantes(request):
    FormEstudiante=FormularioEstudiante() # Almacenas el formulario importado en la variable formulario_estudiantes
    if request.method=="POST": # pregunta que si el request es de tipo post
        FormEstudiante=FormularioEstudiante(data=request.POST) # Pasamos la petición al formulario para luego poder hacer las validaciones del lado del servidor
        if FormEstudiante.is_valid(): # Si es válido puedes acceder a los datos limpios (es decir, validados) a través de la propiedad cleaned_data
            estudiante=Estudiante() # creación del objeto de la clase Estudiante importada de models.py
            estudiante.id=FormEstudiante.cleaned_data['id']
            estudiante.nombre=FormEstudiante.cleaned_data['nombre']
            estudiante.email=FormEstudiante.cleaned_data['email']
            estudiante.direccion=FormEstudiante.cleaned_data['direccion']
            estudiante.tfno=FormEstudiante.cleaned_data['tfno']
            estudiante.save()
            return redirect("/administrarestudiantes/?isvalid") # Al final del if se redirecciona a otra url para confirmar que se ha limpiado y enviado la información a la base de datos
        
    estudiantes=Estudiante.objects.all()
    
    queryall = request.GET.get('b')
    if queryall:
        estudiantes = estudiantes.filter(
            Q(id__icontains=queryall) |
            Q(nombre__icontains=queryall) |
            Q(email__icontains=queryall) |
            Q(direccion__icontains=queryall) |
            Q(tfno__icontains=queryall) |
            Q(estatus__icontains=queryall) 
        )        
        
    # Filtros
    filtro = request.GET.get('filtro')
    if filtro:
        if filtro == 'habilitados':
            estudiantes = estudiantes.filter(estatus__exact='Habilitado')
        elif filtro == 'deshabilitados':
            estudiantes = estudiantes.filter(estatus__exact='Deshabilitado')
    
    # Definir el número de elementos por página
    elementos_por_pagina = 5
    paginator = Paginator(estudiantes, elementos_por_pagina)

    # Obtener el número de página desde la consulta GET, si no se especifica, será la página 1
    page = request.GET.get('page')
    
    try:
        pagina_obj = paginator.get_page(page)
    except PageNotAnInteger:
        # Si el parámetro page no es un entero, mostrar la primera página
        pagina_obj = paginator.get_page(1)
    except EmptyPage:
        # Si la página está fuera del rango, mostrar la última página
        pagina_obj = paginator.get_page(paginator.num_pages)
    
    # Se renderiza la plantilla con todos los campos del formulario creado
    return render(request, "administrarestudiantes/administrarestudiantes.html", {'formE':FormEstudiante, 'estudiantes': estudiantes, 'pagina_obj':pagina_obj})

def editar_estudiantes(request, id):

    estudiantes = Estudiante.objects.get(id = id)
    return render(request, "administrarestudiantes/editarestudiante.html", {'estudiantes': estudiantes})
    

def estudiante_editado(request, id):
    #Para el Listado

    if request.method=="POST":
       
        estudiante = Estudiante.objects.get(id = id)
        estudiante.nombre = request.POST['txtnom']
        estudiante.direccion = request.POST['txtdir']
        estudiante.tfno = request.POST['txttfn']
        estudiante.email = request.POST['txtemail']
        estudiante.save()
        
    return redirect('/administrarestudiantes/?isedited')


def cambiar_estatus(request, estudiante_id):
    estudiante = Estudiante.objects.get(id=estudiante_id)
    if estudiante.estatus == 'Habilitado':
        estudiante.estatus = 'Deshabilitado'
    else:
        estudiante.estatus = 'Habilitado'
    estudiante.save()
    return redirect('/administrarestudiantes/')