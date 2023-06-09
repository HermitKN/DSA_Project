from django.db import models

# Create your models here.

class Estudiante(models.Model):
    cedula=models.CharField(max_length=30)
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50)
    email=models.EmailField(blank=True, null=True)
    tfn=models.CharField(max_length=15)
    fecha=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    codigo=models.CharField(max_length=20)
    nombre=models.CharField(max_length=30)
    autor=models.CharField(max_length=30)
    seccion=models.CharField(max_length=20)
    fecha=models.DateTimeField(auto_now_add=True)

class Prestamo(models.Model):
    numero=models.IntegerField()
    codigo=models.CharField(max_length=20)
    fecha=models.DateTimeField(auto_now_add=True)
    limite=models.DateTimeField(verbose_name="Fecha límite")
    nombre=models.CharField(max_length=30, verbose_name="Nombre del estudiante")
