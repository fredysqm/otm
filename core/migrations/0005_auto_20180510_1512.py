# Generated by Django 2.0.5 on 2018-05-10 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20180507_1758'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marcacomercial',
            name='verificacion_obj',
        ),
        migrations.RemoveField(
            model_name='marcacomercialcuenta',
            name='verificacion_obj',
        ),
        migrations.RemoveField(
            model_name='proveedor',
            name='verificacion_obj',
        ),
    ]