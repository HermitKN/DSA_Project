# Generated by Django 4.2.1 on 2023-07-01 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AdministrarLibros', '0004_libro_cantidadext'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libro',
            name='cantidad',
        ),
    ]
