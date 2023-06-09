from django.contrib import admin
from GenerarPrestamo.models import Estudiante, Libro, Prestamo

# Register your models here.
class EstudiantesAdmin(admin.ModelAdmin):
    list_display=("cedula", "nombre", "direccion", "email", "tfn", "fecha")
    search_fields=("cedula", "nombre", "direccion", "email", "tfn", "fecha")
    list_filter=("nombre", "fecha")

class LibrosAdmin(admin.ModelAdmin):
    list_display=("codigo", "nombre", "autor", "seccion", "fecha")
    search_fields=("codigo", "nombre", "autor", "seccion", "fecha")
    list_filter=("seccion", "autor", "fecha")

class PrestamosAdmin(admin.ModelAdmin):
    list_display=("numero", "codigo", "fecha", "limite", "nombre")
    search_fields=("numero", "codigo", "nombre")
    list_filter=("fecha", "limite")
    date_hierarchy=("limite")

admin.site.register(Estudiante, EstudiantesAdmin)
admin.site.register(Libro, LibrosAdmin)
admin.site.register(Prestamo, PrestamosAdmin)
