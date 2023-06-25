from django.contrib import admin
from GenerarPrestamo.models import Prestamo

# Register your models here.

class PrestamosAdmin(admin.ModelAdmin):
    list_display=("nota", "estudiante", "libro", "limite", "fecha")
    search_fields=("nota", "estudiante", "libro")
    list_filter=("fecha", "limite")
    date_hierarchy=("limite")

admin.site.register(Prestamo, PrestamosAdmin)

