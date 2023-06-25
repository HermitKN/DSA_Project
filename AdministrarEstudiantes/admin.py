from django.contrib import admin
from .models import Estudiante

# Register your models here.

class EstudiantesAdmin(admin.ModelAdmin):
    list_display=("id", "nombre", "email", "direccion", "tfno", "fecha")
    search_fields=("id", "nombre", "email", "direccion", "tfno")
    list_filter=("nombre", "fecha", "direccion")
    date_hierarchy=("fecha")

admin.site.register(Estudiante, EstudiantesAdmin)
