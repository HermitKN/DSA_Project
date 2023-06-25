from django.shortcuts import render
from GenerarPrestamo.models import Prestamo

# Create your views here.

def notas_prestamo(request):

    notas=Prestamo.objects.all()
    return render(request, "notasprestamo/notasprestamo.html", {'notas':notas})