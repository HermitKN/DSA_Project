from django.shortcuts import render, redirect
from .forms import FormularioPrestamo
from .models import Prestamo
# Create your views here.

def generar_prestamo(request):

    formulario_prestamo=FormularioPrestamo()
    if request.method=="POST":
        formulario_prestamo=FormularioPrestamo(data=request.POST)
        if formulario_prestamo.is_valid():
            prestamo=Prestamo()
            prestamo.cedula=formulario_prestamo.cleaned_data['cedula']
            prestamo.codigo=formulario_prestamo.cleaned_data['codigo']
            prestamo.limite=formulario_prestamo.cleaned_data['limite']
            prestamo.save()
            return redirect("/generarprestamo/?isvalid")
        else:
            formulario_prestamo=FormularioPrestamo()
    prestamos=Prestamo.objects.last()
    return render(request, "generarprestamo/generarprestamo.html", {'myForm':formulario_prestamo, 'prestamos': prestamos})