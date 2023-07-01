from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Libro(models.Model):# Tabla con el nombre Libro

    nombre=models.CharField(max_length=50, verbose_name="Nombre del Libro")
    id=models.CharField(max_length=30, verbose_name="Cota del Libro", primary_key=True)
    autor=models.CharField(max_length=50, verbose_name="Autor del libro")
    tipo=models.CharField(max_length=15, verbose_name="Autor del libro")
    cantidad=models.PositiveIntegerField(validators=[MinValueValidator(1)], verbose_name="Copias Internas")
    cantidadext=models.PositiveIntegerField(validators=[MinValueValidator(1)], verbose_name="Copias Externas")
    categoria=models.CharField(max_length=20, verbose_name="Categoria del Libro")
    fecha=models.DateTimeField(auto_now_add=True, verbose_name="Fecha del Ingreso")

    def __str__(self):
        return self.id
    class Meta:
        verbose_name='libro'
        verbose_name_plural='libros'
