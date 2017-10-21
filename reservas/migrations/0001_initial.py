# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-21 11:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=255)),
                ('fecha', models.DateField()),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('estado', models.CharField(default='A', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='ReservaDetalle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('detalle', models.CharField(max_length=50)),
                ('cantidad', models.PositiveIntegerField()),
                ('precio', models.PositiveIntegerField()),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('reserva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservas.Reserva')),
            ],
        ),
    ]
