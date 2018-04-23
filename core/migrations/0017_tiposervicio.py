# Generated by Django 2.0.4 on 2018-04-19 10:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20180419_1015'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoServicio',
            fields=[
                ('id', models.CharField(help_text='Siglas del tipo de servicio', max_length=3, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator('^[a-zA-Z0-9]{3}$', message='Ingrese siglas válidas.')], verbose_name='Siglas')),
                ('nombre', models.CharField(help_text='Nombre del tipo de servicio', max_length=50, validators=[django.core.validators.RegexValidator('^[a-zA-Z0-9áéíóúñÁÉÍÓÚÑ., \\-]+$', message='Ingrese un nombre válido.')], verbose_name='Nombre')),
                ('_estado_obj', models.CharField(choices=[('A', 'Activo'), ('S', 'Suspendido')], default='A', max_length=1)),
                ('_creado', models.DateTimeField(auto_now_add=True)),
                ('_modificado', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'tipos de servicio',
                'verbose_name': 'tipo de servicio',
            },
        ),
    ]
