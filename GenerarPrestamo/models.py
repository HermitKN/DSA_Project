from django.db import models
from AdministrarLibros.models import Libro
from AdministrarEstudiantes.models import Estudiante

# Create your models here.

class Prestamo(models.Model):
    nota = models.AutoField(primary_key=True, verbose_name="Nota de Prestamo")
    estudiante=models.ForeignKey(Estudiante, on_delete=models.CASCADE, verbose_name="Estudiante")
    libro=models.ForeignKey(Libro, on_delete=models.CASCADE, verbose_name="Libro")
    limite=models.DateField(verbose_name="Fecha límite de entrega")
    fecha=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.nota)

    class Meta:
        verbose_name='prestamo'
        verbose_name_plural='prestamos'
