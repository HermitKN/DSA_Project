from django.shortcuts import render, redirect, get_object_or_404
from GenerarPrestamo.models import Prestamo

# Create your views here.

def notas_prestamo(request):
    if request.method=="POST":
        prestamo_id = request.POST.get('prestamo_id')
        prestamo = get_object_or_404(Prestamo, id=prestamo_id)
        if not prestamo.devuelto:
            prestamo.devuelto = True
            prestamo.save()

            # Actualizar la cantidad del libro
            libro = prestamo.libro
            if prestamo.tipo == 'Interno':
                libro.cantidadint += prestamo.cantidad
            else:
                libro.cantidadext += prestamo.cantidad
            libro.save()
            return redirect('/notasprestamo/?true')
    
    notas=Prestamo.objects.all()
    return render(request, "notasprestamo/notasprestamo.html", {'notas':notas})

def cambiar_penalizacion(request, prestamo_id):
    #if request.method=="POST":
    prestamo = Prestamo.objects.get(id=prestamo_id)
    
    prestamo.penalizacion = 'Penalización semanal'
    prestamo.save()
    return redirect('/notasprestamo/')

