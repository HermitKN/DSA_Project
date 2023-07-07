from django.shortcuts import render, redirect, get_object_or_404
from GenerarPrestamo.models import Prestamo

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
    return render(request, "notasprestamo/notasprestamo.html", {'notas':notas})



