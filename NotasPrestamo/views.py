from django.shortcuts import render, redirect, get_object_or_404
from GenerarPrestamo.models import Prestamo
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.utils.dateparse import parse_date
from datetime import datetime, timedelta
# Create your views here.

def notas_prestamo(request):
    if request.method=="POST":
        prestamo_id = request.POST.get('prestamo_id')
        prestamo = get_object_or_404(Prestamo, id=prestamo_id)
        if not prestamo.devuelto:
            prestamo.devuelto = True
            cantidad_devuelta = int(request.POST.get('cantidad_devuelta'))
            prestamo.cantidad_devuelta = cantidad_devuelta
            if prestamo.cantidad_devuelta != prestamo.cantidad:
                prestamo.penalizacion = 'Penalización semanal'
                prestamo.devuelto = False
            prestamo.save()
            
            # Actualizar la cantidad del libro
            libro = prestamo.libro
            if prestamo.tipo == 'Interno':
                libro.cantidadint += prestamo.cantidad_devuelta
            else:
                libro.cantidadext += prestamo.cantidad_devuelta
            libro.save()
            return redirect('/notasprestamo/?true')
    
    
    notas=Prestamo.objects.all()
    
    query = request.GET.get('q')
    if query:
        notas = notas.filter(
            Q(id__icontains=query) |
            Q(estudiante__id__icontains=query) |
            Q(libro__id__icontains=query) |
            Q(tipo__icontains=query) |
            Q(funcionario__username__icontains=query) |
            Q(penalizacion__icontains=query) 
        )     
    else:
        notas = Prestamo.objects.all()
        
    # Filtros
    filtro = request.GET.get('filtro')
    if filtro:
        if filtro == 'internos':
            notas = notas.filter(tipo__exact='Interno')
        elif filtro == 'externos':
            notas = notas.filter(tipo__exact='Externo')
        elif filtro == 'completadas':
            notas = notas.filter(devuelto__exact=True)
        elif filtro == 'incompletadas':
            notas = notas.filter(devuelto__exact=False, penalizacion__exact='Penalización semanal')
        elif filtro == 'pendientes':
            notas = notas.filter(devuelto__exact=False, penalizacion__exact='Sin penalización')
    
    # Definir el número de elementos por página
    elementos_por_pagina = 5
    paginator = Paginator(notas, elementos_por_pagina)

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
    
    return render(request, "notasprestamo/notasprestamo.html", {'notas':notas, 'pagina_obj':pagina_obj})





