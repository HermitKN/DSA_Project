# Generated by Django 4.2.1 on 2023-06-21 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('GenerarPrestamo', '0002_delete_prestamo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=20, verbose_name='CI del Estudiante')),
                ('codigo', models.CharField(max_length=20)),
                ('limite', models.DateField()),
            ],
            options={
                'verbose_name': 'prestamo',
                'verbose_name_plural': 'prestamos',
            },
        ),
    ]
