# Generated by Django 4.2.1 on 2023-06-25 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdministrarLibros', '0002_alter_libro_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='id',
            field=models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='ID del Libro'),
        ),
    ]
