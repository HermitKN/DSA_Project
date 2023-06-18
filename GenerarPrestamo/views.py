from django.shortcuts import render
from .forms import FormularioPrestamo
# Create your views here.

def generar_prestamo(request):

    formulario_prestamo=FormularioPrestamo()
    return render(request, "generarprestamo/generarprestamo.html", {'myForm':formulario_prestamo})