# Generated by Django 4.2.1 on 2023-07-01 16:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdministrarLibros', '0005_remove_libro_cantidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='cantidadint',
            field=models.PositiveIntegerField(default='10', validators=[django.core.validators.MinValueValidator(1)], verbose_name='Copias Internas'),
            preserve_default=False,
        ),
    ]
