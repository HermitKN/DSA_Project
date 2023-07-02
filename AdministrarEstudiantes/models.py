from django.db import models

# Create your models here.

class Estudiante(models.Model):# Creación de la tabla con el nombre Estudiante
    # Campos de la tabla
    id = models.CharField(primary_key=True, max_length=20, verbose_name="CI del Estudiante")
    nombre=models.CharField(max_length=20, verbose_name="Nombre del Estudiante")
    email=models.EmailField(max_length=50, verbose_name="Correo Electrónico")
    direccion=models.CharField(max_length=50, verbose_name="Dirección del Estudiante")
    tfno=models.CharField(max_length=20, verbose_name="Número Telefónico")
    fecha=models.DateTimeField(auto_now_add=True, verbose_name="Fecha del Registro")
    devoluciones=models.IntegerField(default=0, verbose_name="Devoluciones")
    estatus = models.CharField(max_length=30, default='Habilitado')

    def __str__(self):
        return self.id

    class Meta:
        verbose_name='estudiante'
        verbose_name_plural='estudiantes'
