from django.db import models

# Create your models here.

class Estudiante(models.Model):
    
    nombre=models.CharField(max_length=20, verbose_name="Nombre del Estudiante")
    cedula=models.CharField(max_length=20, verbose_name="CI del Estudiante")
    email=models.EmailField(max_length=20, verbose_name="Correo Electrónico")
    direccion=models.CharField(max_length=50, verbose_name="Dirección del Estudiante")
    tfno=models.CharField(max_length=20, verbose_name="Número Telefónico")
    fecha=models.DateTimeField(auto_now_add=True, verbose_name="Fecha del Registro")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name='estudiante'
        verbose_name_plural='estudiantes'
