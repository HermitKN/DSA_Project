# Generated by Django 4.2.1 on 2023-06-25 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdministrarEstudiantes', '0004_alter_estudiante_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='email',
            field=models.EmailField(max_length=50, verbose_name='Correo Electrónico'),
        ),
    ]