# Generated by Django 2.0.3 on 2018-03-27 11:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20180327_1141'),
    ]

    operations = [
        migrations.CreateModel(
            name='Moneda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre de la moneda', max_length=60, validators=[django.core.validators.RegexValidator('^[a-zA-Z0-9áéíóúñÁÉÍÓÚÑ., \\-]+$', message='Ingrese un nombre válido.')], verbose_name='Nombre')),
                ('simbolo', models.CharField(help_text='Símbolo de la moneda', max_length=3, validators=[django.core.validators.MinLengthValidator(1, message='Ingrese un símbolo válido.')], verbose_name='Símbolo')),
                ('_creado', models.DateTimeField(auto_now_add=True)),
                ('_modificado', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'moneda',
                'ordering': ('nombre',),
                'verbose_name_plural': 'monedas',
            },
        ),
        migrations.AlterUniqueTogether(
            name='moneda',
            unique_together={('nombre',)},
        ),
    ]
