# Generated by Django 2.0.3 on 2018-03-27 15:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20180327_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operador',
            name='id',
            field=models.CharField(help_text='Siglas del operador', max_length=6, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator('^[a-zA-Z0-9]+$', message='Ingrese siglas válidas.'), django.core.validators.MinLengthValidator(2)], verbose_name='Siglas'),
        ),
    ]