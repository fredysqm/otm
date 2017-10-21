from django.db import models
from django.core import validators


class TipoDocProveedor(models.Model):
    siglas = models.CharField (
        max_length=3,
        verbose_name='Siglas',
        help_text='Siglas del tipo de documento de proveedor',
        validators=[
            validators.RegexValidator('^[a-zA-Z0-9]{3}$',
                message='Ingrese siglas válidas.'
            ),
        ]
    )

    nombre = models.CharField (
        max_length=50,
        verbose_name='Nombre',
        help_text='Nombre del documento de proveedor',
        validators=[
            validators.RegexValidator('^[a-zA-Z0-9áéíóúñÁÉÍÓÚÑ., \-]+$',
                message='Ingrese un nombre válido.'
            ),
        ]
    )

    def clean(self):
        self.siglas = ' '.join(self.siglas.upper().split())
        self.nombre = ' '.join(self.nombre.upper().split())

    def __str__(self):
        return ('%s' % (self.siglas,))

    class Meta:
        unique_together = ( ('siglas',), ('nombre',) )
        verbose_name = ('tipo de documento proveedor')
        verbose_name_plural = ('tipos de documento proveedor')


class Proveedor(models.Model):
    razon_social = models.CharField (
        max_length=60,
        verbose_name='Razón social',
        help_text='Nombre o razón social de la persona o empresa',
        validators=[
            validators.RegexValidator('^[a-zA-Z0-9áéíóúñÁÉÍÓÚÑ., \-]+$',
                message='Ingrese una razón social válida.'
            ),
        ]
    )

    tipo_documento = models.ForeignKey(
        TipoDocProveedor,
        verbose_name='Tipo de documento',
    )

    nro_documento = models.CharField(
        max_length=11,
        verbose_name='Número de documento',
        validators=[
            validators.RegexValidator('^[0-9]{8,11}$',
                message='Ingrese un número de documento válido.'
            ),
        ]
    )

    direccion = models.CharField(
        max_length=100,
        blank = True,
        verbose_name='Dirección',
        help_text='Dirección de la persona o empresa',
        validators=[
            validators.RegexValidator('^[a-zA-Z0-9áéíóúñÁÉÍÓÚÑ., \-]+$',
                message='Ingrese una dirección válida.'
            ),
        ]
    )

    def clean(self):
        self.razon_social = ' '.join(self.razon_social.upper().split())
        self.direccion = ' '.join(self.direccion.upper().split())
        if self.tipo_documento.pk == 1: #RUC
            if len(self.nro_documento) != 11:
                raise validators.ValidationError('Número de documento RUC debe tener 11 dígitos.')
        elif self.tipo_documento.pk == 2: #DNI
            if len(self.nro_documento) != 8:
                raise validators.ValidationError('Número de documento DNI debe tener 8 dígitos.')
        elif self.tipo_documento.pk == 3: #NIT
            if len(self.nro_documento) != 10:
                raise validators.ValidationError("Número de documento NIT debe tener 10 dígitos.")

    def __str__(self):
        return ('%s (%s %s)' % (self.razon_social, self.tipo_documento, self.nro_documento))

    class Meta:
        unique_together = ( ('razon_social',), ('nro_documento',) )
        verbose_name = ('proveedor')
        verbose_name_plural = ('proveedores')