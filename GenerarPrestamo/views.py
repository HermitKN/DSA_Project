from django.shortcuts import render

# Create your views here.

def generar_prestamo(request):

    return render(request, "generarprestamo/generarprestamo.html")