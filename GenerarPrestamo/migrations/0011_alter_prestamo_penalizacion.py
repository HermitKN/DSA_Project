# Generated by Django 4.2.1 on 2023-07-02 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GenerarPrestamo', '0010_prestamo_penalizacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='penalizacion',
            field=models.CharField(default='Sin penalización', max_length=50),
        ),
    ]
