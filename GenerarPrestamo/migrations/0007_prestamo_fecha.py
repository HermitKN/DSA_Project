# Generated by Django 4.2.1 on 2023-06-23 04:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('GenerarPrestamo', '0006_rename_id_prestamo_nota'),
    ]

    operations = [
        migrations.AddField(
            model_name='prestamo',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]