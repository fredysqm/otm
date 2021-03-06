# Generated by Django 2.0.5 on 2018-05-07 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_proveedor_domicilio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='banco',
            old_name='_creado',
            new_name='creado',
        ),
        migrations.RenameField(
            model_name='banco',
            old_name='_estado_obj',
            new_name='estado_obj',
        ),
        migrations.RenameField(
            model_name='banco',
            old_name='_modificado',
            new_name='modificado',
        ),
        migrations.RenameField(
            model_name='categoriaservicio',
            old_name='_creado',
            new_name='creado',
        ),
        migrations.RenameField(
            model_name='categoriaservicio',
            old_name='_estado_obj',
            new_name='estado_obj',
        ),
        migrations.RenameField(
            model_name='categoriaservicio',
            old_name='_modificado',
            new_name='modificado',
        ),
        migrations.RenameField(
            model_name='ciudad',
            old_name='_creado',
            new_name='creado',
        ),
        migrations.RenameField(
            model_name='ciudad',
            old_name='_estado_obj',
            new_name='estado_obj',
        ),
        migrations.RenameField(
            model_name='ciudad',
            old_name='_modificado',
            new_name='modificado',
        ),
        migrations.RenameField(
            model_name='idioma',
            old_name='_creado',
            new_name='creado',
        ),
        migrations.RenameField(
            model_name='idioma',
            old_name='_estado_obj',
            new_name='estado_obj',
        ),
        migrations.RenameField(
            model_name='idioma',
            old_name='_modificado',
            new_name='modificado',
        ),
        migrations.RenameField(
            model_name='localidad',
            old_name='_creado',
            new_name='creado',
        ),
        migrations.RenameField(
            model_name='localidad',
            old_name='_estado_obj',
            new_name='estado_obj',
        ),
        migrations.RenameField(
            model_name='localidad',
            old_name='_modificado',
            new_name='modificado',
        ),
        migrations.RenameField(
            model_name='marcacomercial',
            old_name='_creado',
            new_name='creado',
        ),
        migrations.RenameField(
            model_name='marcacomercial',
            old_name='_estado_obj',
            new_name='estado_obj',
        ),
        migrations.RenameField(
            model_name='marcacomercial',
            old_name='_modificado',
            new_name='modificado',
        ),
        migrations.RenameField(
            model_name='marcacomercial',
            old_name='_verificacion_obj',
            new_name='verificacion_obj',
        ),
        migrations.RenameField(
            model_name='marcacomercialcuenta',
            old_name='_creado',
            new_name='creado',
        ),
        migrations.RenameField(
            model_name='marcacomercialcuenta',
            old_name='_estado_obj',
            new_name='estado_obj',
        ),
        migrations.RenameField(
            model_name='marcacomercialcuenta',
            old_name='_modificado',
            new_name='modificado',
        ),
        migrations.RenameField(
            model_name='marcacomercialcuenta',
            old_name='_verificacion_obj',
            new_name='verificacion_obj',
        ),
        migrations.RenameField(
            model_name='modalidadpago',
            old_name='_creado',
            new_name='creado',
        ),
        migrations.RenameField(
            model_name='modalidadpago',
            old_name='_estado_obj',
            new_name='estado_obj',
        ),
        migrations.RenameField(
            model_name='modalidadpago',
            old_name='_modificado',
            new_name='modificado',
        ),
        migrations.RenameField(
            model_name='moneda',
            old_name='_creado',
            new_name='creado',
        ),
        migrations.RenameField(
            model_name='moneda',
            old_name='_estado_obj',
            new_name='estado_obj',
        ),
        migrations.RenameField(
            model_name='moneda',
            old_name='_modificado',
            new_name='modificado',
        ),
        migrations.RenameField(
            model_name='operador',
            old_name='_creado',
            new_name='creado',
        ),
        migrations.RenameField(
            model_name='operador',
            old_name='_estado_obj',
            new_name='estado_obj',
        ),
        migrations.RenameField(
            model_name='operador',
            old_name='_modificado',
            new_name='modificado',
        ),
        migrations.RenameField(
            model_name='pais',
            old_name='_creado',
            new_name='creado',
        ),
        migrations.RenameField(
            model_name='pais',
            old_name='_estado_obj',
            new_name='estado_obj',
        ),
        migrations.RenameField(
            model_name='pais',
            old_name='_modificado',
            new_name='modificado',
        ),
        migrations.RenameField(
            model_name='proveedor',
            old_name='_creado',
            new_name='creado',
        ),
        migrations.RenameField(
            model_name='proveedor',
            old_name='_estado_obj',
            new_name='estado_obj',
        ),
        migrations.RenameField(
            model_name='proveedor',
            old_name='_modificado',
            new_name='modificado',
        ),
        migrations.RenameField(
            model_name='proveedor',
            old_name='_verificacion_obj',
            new_name='verificacion_obj',
        ),
        migrations.RenameField(
            model_name='tipocuentabanco',
            old_name='_creado',
            new_name='creado',
        ),
        migrations.RenameField(
            model_name='tipocuentabanco',
            old_name='_estado_obj',
            new_name='estado_obj',
        ),
        migrations.RenameField(
            model_name='tipocuentabanco',
            old_name='_modificado',
            new_name='modificado',
        ),
        migrations.RenameField(
            model_name='tipodocproveedor',
            old_name='_creado',
            new_name='creado',
        ),
        migrations.RenameField(
            model_name='tipodocproveedor',
            old_name='_estado_obj',
            new_name='estado_obj',
        ),
        migrations.RenameField(
            model_name='tipodocproveedor',
            old_name='_modificado',
            new_name='modificado',
        ),
    ]
