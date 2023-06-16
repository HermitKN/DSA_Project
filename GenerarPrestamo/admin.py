from django.contrib import admin
from GenerarPrestamo.models import Prestamo

# Register your models here.

class PrestamosAdmin(admin.ModelAdmin):
    list_display=("numero", "codigo", "fecha", "limite", "cedula")
    search_fields=("numero", "codigo", "cedula")
    list_filter=("fecha", "limite")
    date_hierarchy=("limite")

admin.site.register(Prestamo, PrestamosAdmin)
