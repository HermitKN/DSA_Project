from django.db import models

# Create your models here.
class Libro(models.Model):# Tabla con el nombre Libro

    nombre=models.CharField(max_length=20, verbose_name="Nombre del Libro")
    id=models.CharField(max_length=20, verbose_name="ID del Libro", primary_key=True)
    autor=models.CharField(max_length=50, verbose_name="Autor del libro")
    tipo=models.CharField(max_length=15, verbose_name="Autor del libro")
    cantidad=models.IntegerField(verbose_name="Cantidad de copias")
    categoria=models.CharField(max_length=20, verbose_name="Categoria del Libro")
    fecha=models.DateTimeField(auto_now_add=True, verbose_name="Fecha del Ingreso")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name='libro'
        verbose_name_plural='libros'

class Tipo(models.Model):

    Tipo1 = models.CharField(max_length=10)
    
