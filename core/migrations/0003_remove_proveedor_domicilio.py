# Generated by Django 2.0.5 on 2018-05-07 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180427_1609'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proveedor',
            name='domicilio',
        ),
    ]
