# Generated by Django 4.2.1 on 2023-06-30 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GenerarPrestamo', '0002_prestamo_funcionario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prestamo',
            old_name='nota',
            new_name='id',
        ),
    ]