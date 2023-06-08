from django.contrib import admin
from GenerarPrestamo.models import Estudiante, Libro, Prestamo

# Register your models here.
class LibrosAdmin(admin.ModelAdmin):
    list_display=("codigo", "nombre", "autor", "seccion")
    search_fields=("codigo", "nombre", "autor", "seccion")
    list_filter=("seccion", "autor")

class PrestamosAdmin(admin.ModelAdmin):
    list_display=("numero", "codigo", "fecha", "limite", "nombre")
    search_fields=("numero", "codigo", "nombre")
    list_filter=("fecha", "limite")
    date_hierarchy=("limite")

admin.site.register(Estudiante)
admin.site.register(Libro, LibrosAdmin)
admin.site.register(Prestamo, PrestamosAdmin)
