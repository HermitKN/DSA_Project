from django.db import models

# Create your models here.

class Prestamo(models.Model):
    nota = models.AutoField(primary_key=True, verbose_name="Nota de Prestamo")
    cedula=models.CharField(max_length=20, verbose_name="CI del Estudiante")
    codigo=models.CharField(max_length=20)
    limite=models.DateField()
    fecha=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.nota)

    class Meta:
        verbose_name='prestamo'
        verbose_name_plural='prestamos'
