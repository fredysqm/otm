# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-20 10:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(blank=True, max_length=255)),
                ('fecha', models.DateTimeField()),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('estado', models.CharField(default='A', max_length=1)),
            ],
        ),
    ]
