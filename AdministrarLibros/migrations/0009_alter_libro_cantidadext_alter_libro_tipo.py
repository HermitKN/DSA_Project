# Generated by Django 4.2.1 on 2023-07-19 20:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdministrarLibros', '0008_alter_libro_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='cantidadext',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Copias Externas'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='tipo',
            field=models.CharField(choices=[('Tesis', 'Tesis'), ('Libros', 'Libro')], max_length=8, verbose_name='Tipo del libro'),
        ),
    ]