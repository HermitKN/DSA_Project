from django.db import models

# Create your models here.

class Estudiante(models.Model):
    cedula=models.CharField(max_length=30)
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50)
    email=models.EmailField(blank=True, null=True)
    tfn=models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    codigo=models.CharField(max_length=20)
    nombre=models.CharField(max_length=30)
    autor=models.CharField(max_length=30)
    seccion=models.CharField(max_length=20)

class Prestamo(models.Model):
    numero=models.IntegerField()
    codigo=models.CharField(max_length=20)
    fecha=models.DateField()
    limite=models.DateField()
    nombre=models.CharField(max_length=30, verbose_name="Nombre del estudiante")
