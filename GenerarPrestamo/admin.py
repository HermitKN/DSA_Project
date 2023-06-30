from django.contrib import admin
from GenerarPrestamo.models import Prestamo

# Register your models here.

class PrestamosAdmin(admin.ModelAdmin):
    list_display=("id", "tipo","estudiante", "libro", "funcionario", "limite", "fecha", "devuelto")
    search_fields=("id", "estudiante", "libro", "funcionario", "devuelto", "tipo")
    list_filter=("fecha", "limite", "funcionario", "devuelto", "tipo")
    date_hierarchy=("limite")

admin.site.register(Prestamo, PrestamosAdmin)

