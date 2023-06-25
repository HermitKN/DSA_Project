from django.shortcuts import render, redirect
from .forms import FormularioPrestamo
from .models import Prestamo
# Create your views here.

def generar_prestamo(request):

    formulario_prestamo=FormularioPrestamo()
    if request.method=="POST":
        formulario_prestamo=FormularioPrestamo(data=request.POST)
        if formulario_prestamo.is_valid():
            formulario_prestamo.cleaned_data['limite']
            formulario_prestamo.save()
            return redirect("/generarprestamo/?isvalid")
        
    prestamos=Prestamo.objects.last()
    return render(request, "generarprestamo/generarprestamo.html", {'myForm':formulario_prestamo, 'prestamos': prestamos})