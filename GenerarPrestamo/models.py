from django.db import models

# Create your models here.

class Prestamo(models.Model):
    #nota=models.IntegerField()
    cedula=models.CharField(max_length=20, verbose_name="CI del Estudiante")
    codigo=models.CharField(max_length=20)
    limite=models.DateField()
    #fecha=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name='prestamo'
        verbose_name_plural='prestamos'
