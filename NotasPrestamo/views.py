from django.shortcuts import render

# Create your views here.

def notas_prestamo(request):

    return render(request, "notasprestamo/notasprestamo.html")