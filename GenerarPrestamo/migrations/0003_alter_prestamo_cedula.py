# Generated by Django 4.2.1 on 2023-06-16 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GenerarPrestamo', '0002_alter_prestamo_cedula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='cedula',
            field=models.BigIntegerField(),
        ),
    ]