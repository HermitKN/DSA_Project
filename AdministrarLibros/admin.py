from django.contrib import admin
from .models import Libro

# Register your models here.

class LibrosAdmin(admin.ModelAdmin):
    list_display=("id", "nombre", "autor", "tipo", "cantidad", "categoria", "fecha")
    search_fields=("id", "nombre", "autor", "tipo", "cantidad", "categoria")
    list_filter=("nombre", "autor", "tipo", "categoria")
    date_hierarchy=("fecha")

admin.site.register(Libro, LibrosAdmin)
