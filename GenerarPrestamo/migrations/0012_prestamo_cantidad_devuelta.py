# Generated by Django 4.2.1 on 2023-07-07 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GenerarPrestamo', '0011_alter_prestamo_penalizacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='prestamo',
            name='cantidad_devuelta',
            field=models.PositiveIntegerField(default=0, verbose_name='Cantidad Devuelta'),
        ),
    ]
