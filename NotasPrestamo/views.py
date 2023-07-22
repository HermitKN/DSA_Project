from django.shortcuts import render, redirect, get_object_or_404
from GenerarPrestamo.models import Prestamo
from django.core.paginator import Paginator

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
    
    # Filtros
    mostrar_penalizados = request.GET.get('penalizados')
    mostrar_no_penalizados = request.GET.get('no_penalizados')
    
    notas=Prestamo.objects.all()
    
    # Filtrar por préstamos con estudiantes penalizados o no penalizados si se especifica el parámetro en la URL
    if mostrar_penalizados is not None:
        notas = notas.filter(penalizacion__exact='Penalización semanal')
        
    if mostrar_no_penalizados is not None:
        notas = notas.filter(penalizacion__exact='Sin penalización')
    
    # Definir el número de elementos por página
    elementos_por_pagina = 5
    paginator = Paginator(notas, elementos_por_pagina)

    # Obtener el número de página desde la consulta GET, si no se especifica, será la página 1
    pagina_numero = request.GET.get('pagina')
    pagina_obj = paginator.get_page(pagina_numero)
    
    return render(request, "notasprestamo/notasprestamo.html", {'notas':notas, 'pagina_obj': pagina_obj})



