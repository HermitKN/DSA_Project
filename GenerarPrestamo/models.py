from django.db import models

# Create your models here.

class Prestamo(models.Model):
    numero=models.IntegerField()
    codigo=models.CharField(max_length=20)
    fecha=models.DateField(auto_now_add=True)
    limite=models.DateField(default='')
    cedula=models.IntegerField(verbose_name="CI del Estudiante")

    class Meta:
        verbose_name='prestamo'
        verbose_name_plural='prestamos'

