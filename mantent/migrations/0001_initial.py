# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-20 16:16
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razon_social', models.CharField(help_text='Nombre o razón social de la persona o empresa', max_length=60, validators=[django.core.validators.RegexValidator('^[a-zA-Z0-9áéíóúñÁÉÍÓÚÑ., \\-]+$', message='Ingrese una razón social válida.')], verbose_name='Razón social')),
                ('nro_documento', models.CharField(max_length=11, validators=[django.core.validators.RegexValidator('^[0-9]{8,11}$', message='Ingrese un número de documento válido.')], verbose_name='Número de documento')),
                ('direccion', models.CharField(blank=True, help_text='Dirección de la persona o empresa', max_length=100, validators=[django.core.validators.RegexValidator('^[a-zA-Z0-9áéíóúñÁÉÍÓÚÑ., \\-]+$', message='Ingrese una dirección válida.')], verbose_name='Dirección')),
            ],
            options={
                'verbose_name': 'proveedor',
                'verbose_name_plural': 'proveedores',
            },
        ),
        migrations.CreateModel(
            name='TipoDocProveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('siglas', models.CharField(help_text='Siglas del tipo de documento de proveedor', max_length=3, validators=[django.core.validators.RegexValidator('^[a-zA-Z0-9]{3}$', message='Ingrese siglas válidas.')], verbose_name='Siglas')),
                ('nombre', models.CharField(help_text='Nombre del documento de proveedor', max_length=50, validators=[django.core.validators.RegexValidator('^[a-zA-Z0-9áéíóúñÁÉÍÓÚÑ., \\-]+$', message='Ingrese un nombre válido.')], verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Tipo de documento proveedor',
                'verbose_name_plural': 'Tipos de documento proveedor',
            },
        ),
        migrations.AlterUniqueTogether(
            name='tipodocproveedor',
            unique_together=set([('nombre',), ('siglas',)]),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='tipo_documento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mantent.TipoDocProveedor', verbose_name='Tipo de documento'),
        ),
        migrations.AlterUniqueTogether(
            name='proveedor',
            unique_together=set([('razon_social',), ('nro_documento',)]),
        ),
    ]
