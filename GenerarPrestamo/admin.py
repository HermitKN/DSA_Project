from django.contrib import admin
from GenerarPrestamo.models import Prestamo

# Register your models here.

class PrestamosAdmin(admin.ModelAdmin):
    list_display=("id", "estudiante", "libro", "limite", "fecha", "funcionario")
    search_fields=("id", "estudiante", "libro", "funcionario")
    list_filter=("fecha", "limite", "funcionario")
    date_hierarchy=("limite")

admin.site.register(Prestamo, PrestamosAdmin)

