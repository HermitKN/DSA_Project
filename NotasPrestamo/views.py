from django.shortcuts import render, get_object_or_404
#from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from GenerarPrestamo.models import Prestamo

# Create your views here.

def notas_prestamo(request):

    notas=Prestamo.objects.all()
    return render(request, "notasprestamo/notasprestamo.html", {'notas':notas})