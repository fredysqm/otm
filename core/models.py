from django.db import models
from django.core import validators
from django.core.exceptions import ObjectDoesNotExist


class Pais(models.Model):
    id = models.CharField (
        primary_key=True,
        max_length=2,
        verbose_name='Siglas',
        help_text='Siglas del país',
        validators=[
            validators.RegexValidator(
                '^[a-zA-Z0-9]{2}$',
                message='Ingrese siglas válidas.'
            ),
        ]
    )

    nombre = models.CharField (
        max_length=60,
        verbose_name='Nombre',
        help_text='Nombre del país',
        validators=[
            validators.RegexValidator(
                '^[a-zA-Z0-9áéíóúñÁÉÍÓÚÑ., \-]+$',
                message='Ingrese un nombre válido.'
            ),
        ]
    )

    _creado = models.DateTimeField(auto_now_add=True,)
    _modificado = models.DateTimeField(auto_now=True,)

    def clean(self, *args, **kwargs):
        super(Pais, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.id = ' '.join(self.id.upper().split())
        self.nombre = ' '.join(self.nombre.upper().split())
        super(Pais, self).save(*args, **kwargs)

    def __str__(self):
        return ('%s (%s)' % (self.nombre, self.id,))

    class Meta:
        unique_together = ( ('nombre',), )
        verbose_name = ('país')
        verbose_name_plural = ('paises')
        ordering = ('nombre',)


class Ciudad(models.Model):
    id = models.CharField (
        primary_key=True,
        max_length=3,
        verbose_name='Siglas',
        help_text='Siglas de la ciudad',
        validators=[
            validators.RegexValidator(
                '^[a-zA-Z0-9]{3}$',
                message='Ingrese siglas válidas.'
            ),
        ]
    )

    pais = models.ForeignKey (
        Pais,
        on_delete=models.CASCADE,
    )

    nombre = models.CharField (
        max_length=60,
        verbose_name='Nombre',
        help_text='Nombre de la ciudad',
        validators=[
            validators.RegexValidator(
                '^[a-zA-Z0-9áéíóúñÁÉÍÓÚÑ., \-]+$',
                message='Ingrese un nombre válido.'
            ),
        ]
    )

    _creado = models.DateTimeField(auto_now_add=True,)
    _modificado = models.DateTimeField(auto_now=True,)

    def clean(self, *args, **kwargs):
        super(Ciudad, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.id = ' '.join(self.id.upper().split())
        self.nombre = ' '.join(self.nombre.upper().split())
        super(Ciudad, self).save(*args, **kwargs)

    def __str__(self):
        return ('%s' % (self.id,))

    class Meta:
        unique_together = ( ('pais','nombre',), )
        verbose_name = ('ciudad')
        verbose_name_plural = ('ciudades')

# class TipoDocProveedor(models.Model):
#     id = models.CharField (
#         primary_key=True,
#         max_length=3,
#         verbose_name='Siglas',
#         help_text='Siglas del tipo de documento de proveedor',
#         validators=[
#             validators.RegexValidator(
#                 '^[a-zA-Z0-9]{3}$',
#                 message='Ingrese siglas válidas.'
#             ),
#         ]
#     )

#     nombre = models.CharField (
#         max_length=100,
#         verbose_name='Nombre',
#         help_text='Nombre del documento de proveedor',
#         validators=[
#             validators.RegexValidator(
#                 '^[a-zA-Z0-9áéíóúñÁÉÍÓÚÑ., \-]+$',
#                 message='Ingrese un nombre válido.'
#             ),
#         ]
#     )

#     def clean(self, *args, **kwargs):
#         super(TipoDocProveedor, self).clean(*args, **kwargs)

#     def save(self, *args, **kwargs):
#         self.id = ' '.join(self.id.upper().split())
#         self.nombre = ' '.join(self.nombre.upper().split())
#         super(TipoDocProveedor, self).save(*args, **kwargs)

#     def __str__(self):
#         return ('%s' % (self.id,))

#     class Meta:
#         unique_together = ( ('nombre',), )
#         verbose_name = ('tipo de documento proveedor')
#         verbose_name_plural = ('tipos de documento proveedor')


# class Proveedor(models.Model):
#     id = models.CharField(
#         primary_key=True,
#         max_length=11,
#         verbose_name='Número de documento',
#         validators=[
#             validators.RegexValidator(
#                 '^[0-9]{8,11}$',
#                 message='Ingrese un número de documento válido.'
#             ),
#         ]
#     )

#     tipo_documento = models.ForeignKey(
#         TipoDocProveedor,
#         verbose_name='Tipo de documento',
#         on_delete=models.PROTECT,
#     )

#     razon_social = models.CharField (
#         max_length=100,
#         verbose_name='Razón social',
#         help_text='Nombre o razón social de la persona o empresa',
#         validators=[
#             validators.RegexValidator(
#                 '^[a-zA-Z0-9áéíóúñÁÉÍÓÚÑ., \-]+$',
#                 message='Ingrese una razón social válida.'
#             ),
#         ]
#     )

#     direccion = models.CharField(
#         max_length=100,
#         blank = True,
#         verbose_name='Dirección',
#         help_text='Dirección de la persona o empresa',
#         validators=[
#             validators.RegexValidator(
#                 '^[a-zA-Z0-9áéíóúñÁÉÍÓÚÑ., \-]+$',
#                 message='Ingrese una dirección válida.'
#             ),
#         ]
#     )

#     _fts = models.CharField(max_length=255,)
#     _creado = models.DateTimeField(auto_now_add=True,)
#     _modificado = models.DateTimeField(auto_now=True,)

#     def clean(self, *args, **kwargs):
#         try:
#             if self.tipo_documento.pk == 'RUC':
#                 if len(self.id) != 11:
#                     raise validators.ValidationError('Número de documento RUC debe tener 11 dígitos.')
#             elif self.tipo_documento.pk == 'DNI':
#                 if len(self.id) != 8:
#                     raise validators.ValidationError('Número de documento DNI debe tener 8 dígitos.')
#             elif self.tipo_documento.pk == 'NIT': #NIT
#                 if len(self.id) != 10:
#                     raise validators.ValidationError("Número de documento NIT debe tener 10 dígitos.")
#         except ObjectDoesNotExist:
#             pass
        
#         super(Proveedor, self).clean(*args, **kwargs)

#     def save(self, *args, **kwargs):
#         self.razon_social = ' '.join(self.razon_social.upper().split())
#         self.direccion = ' '.join(self.direccion.upper().split())
#         self._fts = '%s %s %s' % (self.id, self.razon_social, self.tipo_documento)
#         super(Proveedor, self).save(*args, **kwargs)

#     def __str__(self):
#         return ('%s (%s %s)' % (self.razon_social, self.tipo_documento, self.id))

#     class Meta:
#         unique_together = ( ('razon_social',), )
#         verbose_name = ('proveedor')
#         verbose_name_plural = ('proveedores')