# Generated by Django 4.2.1 on 2023-06-30 23:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdministrarLibros', '0002_alter_libro_cantidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='cantidad',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Copias Int'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='cantidadext',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Copias Ext'),
        ),
        
    ]
