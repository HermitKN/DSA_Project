# Generated by Django 4.2.1 on 2023-06-25 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdministrarEstudiantes', '0002_alter_estudiante_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudiante',
            name='cedula',
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Nota de Prestamo'),
        ),
    ]
