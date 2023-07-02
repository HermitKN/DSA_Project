from django.contrib import admin
from GenerarPrestamo.models import Prestamo

# Register your models here.

class PrestamosAdmin(admin.ModelAdmin):
    list_display=("id", "tipo","estudiante", "libro", "cantidad", "funcionario", "limite", "fecha", "penalizacion", "devuelto")
    search_fields=("id", "estudiante", "libro", "funcionario", "devuelto", "tipo", "cantidad")
    list_filter=("fecha", "limite", "funcionario", "devuelto", "tipo", "penalizacion")
    date_hierarchy=("limite")

admin.site.register(Prestamo, PrestamosAdmin)

