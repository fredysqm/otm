# Generated by Django 2.0.3 on 2018-03-27 12:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20180327_1157'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre del banco', max_length=60, validators=[django.core.validators.RegexValidator('^[a-zA-Z0-9áéíóúñÁÉÍÓÚÑ., \\-]+$', message='Ingrese un nombre válido.')], verbose_name='Nombre')),
                ('_creado', models.DateTimeField(auto_now_add=True)),
                ('_modificado', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'banco',
                'ordering': ('nombre',),
                'verbose_name_plural': 'bancos',
            },
        ),
        migrations.AlterUniqueTogether(
            name='banco',
            unique_together={('nombre',)},
        ),
    ]
