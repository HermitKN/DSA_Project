from django.shortcuts import render, redirect
from .forms import FormularioPrestamo
from .models import Prestamo
# Create your views here.

def generar_prestamo(request):

    formulario_prestamo=FormularioPrestamo()
    if request.method=="POST":
        formulario_prestamo=FormularioPrestamo(data=request.POST)
        if formulario_prestamo.is_valid():
            nota=request.POST.get("nota")
            cedula=request.POST.get("cedula")
            codigo=request.POST.get("codigo")
            limite=request.POST.get("limite")
            prestamo=Prestamo(nota, cedula, codigo, limite)
            prestamo.save()
            return redirect("/generarprestamo/?isvalid")
    return render(request, "generarprestamo/generarprestamo.html", {'myForm':formulario_prestamo})