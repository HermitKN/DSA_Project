# Generated by Django 4.2.1 on 2023-06-23 03:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GenerarPrestamo', '0005_alter_prestamo_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prestamo',
            old_name='id',
            new_name='nota',
        ),
    ]
