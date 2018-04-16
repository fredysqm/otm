from django.db import models
from django.core import validators
from django.core.exceptions import ObjectDoesNotExist


_ESTADO_OBJ = (
    ('A', 'Activo'),
    ('S', 'Suspendido'),
)

_VERIFICACION_OBJ = (
    ('S', 'Si'),
    ('N', 'No'),
)

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

    _estado_obj = models.CharField(max_length=1, choices=_ESTADO_OBJ, default='A')
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
        on_delete=models.PROTECT,
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

    _estado_obj = models.CharField(max_length=1, choices=_ESTADO_OBJ, default='A')
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


class Idioma(models.Model):
    id = models.CharField (
        primary_key=True,
        max_length=2,
        verbose_name='Siglas',
        help_text='Siglas del idioma',
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
        help_text='Nombre del idioma',
        validators=[
            validators.RegexValidator(
                '^[a-zA-Z0-9áéíóúñÁÉÍÓÚÑ., \-]+$',
                message='Ingrese un nombre válido.'
            ),
        ]
    )

    _estado_obj = models.CharField(max_length=1, choices=_ESTADO_OBJ, default='A')
    _creado = models.DateTimeField(auto_now_add=True,)
    _modificado = models.DateTimeField(auto_now=True,)

    def clean(self, *args, **kwargs):
        super(Idioma, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.id = ' '.join(self.id.upper().split())
        self.nombre = ' '.join(self.nombre.upper().split())
        super(Idioma, self).save(*args, **kwargs)

    def __str__(self):
        return ('%s (%s)' % (self.nombre, self.id,))

    class Meta:
        unique_together = ( ('nombre',), )
        verbose_name = ('idioma')
        verbose_name_plural = ('idiomas')
        ordering = ('nombre',)


class Moneda(models.Model):
    nombre = models.CharField (
        max_length=60,
        verbose_name='Nombre',
        help_text='Nombre de la moneda',
        validators=[
            validators.RegexValidator(
                '^[a-zA-Z0-9áéíóúñÁÉÍÓÚÑ., \-]+$',
                message='Ingrese un nombre válido.'
            ),
        ]
    )

    simbolo = models.CharField (
        max_length=3,
        verbose_name='Símbolo',
        help_text='Símbolo de la moneda',
    )

    _estado_obj = models.CharField(max_length=1, choices=_ESTADO_OBJ, default='A')
    _creado = models.DateTimeField(auto_now_add=True,)
    _modificado = models.DateTimeField(auto_now=True,)

    def clean(self, *args, **kwargs):
        super(Moneda, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.nombre = ' '.join(self.nombre.upper().split())
        self.simbolo = ' '.join(self.simbolo.upper().split())
        super(Moneda, self).save(*args, **kwargs)

    def __str__(self):
        return ('%s (%s)' % (self.nombre, self.simbolo,))

    class Meta:
        unique_together = ( ('nombre',), )
        verbose_name = ('moneda')
        verbose_name_plural = ('monedas')
        ordering = ('nombre',)


class Banco(models.Model):
    nombre = models.CharField (
        max_length=60,
        verbose_name='Nombre',
        help_text='Nombre del banco',
        validators=[
            validators.RegexValidator(
                '^[a-zA-Z0-9áéíóúñÁÉÍÓÚÑ., \-]+$',
                message='Ingrese un nombre válido.'
            ),
        ]
    )

    _estado_obj = models.CharField(max_length=1, choices=_ESTADO_OBJ, default='A')
    _creado = models.DateTimeField(auto_now_add=True,)
    _modificado = models.DateTimeField(auto_now=True,)

    def clean(self, *args, **kwargs):
        super(Banco, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.nombre = ' '.join(self.nombre.upper().split())
        super(Banco, self).save(*args, **kwargs)

    def __str__(self):
        return ('%s' % (self.nombre,))

    class Meta:
        unique_together = ( ('nombre',), )
        verbose_name = ('banco')
        verbose_name_plural = ('bancos')
        ordering = ('nombre',)


class Operador(models.Model):
    id = models.CharField (
        primary_key=True,
        max_length=6,
        verbose_name='Siglas',
        help_text='Siglas del operador',
        validators=[
            validators.RegexValidator(
                '^[a-zA-Z0-9]+$',
                message='Ingrese siglas válidas.'
            ),
            validators.MinLengthValidator(
                2
            ),
        ]
    )

    nombre = models.CharField (
        max_length=60,
        verbose_name='Nombre',
        help_text='Nombre del operador',
        validators=[
            validators.RegexValidator(
                '^[a-zA-Z0-9áéíóúñÁÉÍÓÚÑ., \-]+$',
                message='Ingrese un nombre válido.'
            ),
        ]
    )

    _estado_obj = models.CharField(max_length=1, choices=_ESTADO_OBJ, default='A')
    _creado = models.DateTimeField(auto_now_add=True,)
    _modificado = models.DateTimeField(auto_now=True,)

    def clean(self, *args, **kwargs):
        super(Operador, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.id = ' '.join(self.id.upper().split())
        self.nombre = ' '.join(self.nombre.upper().split())
        super(Operador, self).save(*args, **kwargs)

    def __str__(self):
        return ('%s' % (self.nombre,))

    class Meta:
        unique_together = ( ('nombre',), )
        verbose_name = ('operador')
        verbose_name_plural = ('operadores')
        ordering = ('nombre',)


class TipoDocProveedor(models.Model):
    id = models.CharField (
        primary_key=True,
        max_length=3,
        verbose_name='Siglas',
        help_text='Siglas del tipo de documento de proveedor',
        validators=[
            validators.RegexValidator(
                '^[a-zA-Z0-9]{3}$',
                message='Ingrese siglas válidas.'
            ),
        ]
    )

    nombre = models.CharField (
        max_length=100,
        verbose_name='Nombre',
        help_text='Nombre del documento de proveedor',
        validators=[
            validators.RegexValidator(
                '^[a-zA-Z0-9áéíóúñÁÉÍÓÚÑ., \-]+$',
                message='Ingrese un nombre válido.'
            ),
        ]
    )

    _estado_obj = models.CharField(max_length=1, choices=_ESTADO_OBJ, default='A')
    _creado = models.DateTimeField(auto_now_add=True,)
    _modificado = models.DateTimeField(auto_now=True,)

    def clean(self, *args, **kwargs):
        super(TipoDocProveedor, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.id = ' '.join(self.id.upper().split())
        self.nombre = ' '.join(self.nombre.upper().split())
        super(TipoDocProveedor, self).save(*args, **kwargs)

    def __str__(self):
        return ('%s' % (self.id,))

    class Meta:
        unique_together = ( ('nombre',), )
        verbose_name = ('tipo de documento proveedor')
        verbose_name_plural = ('tipos de documento proveedor')
        ordering = ('nombre',)


class Proveedor(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=11,
        verbose_name='Número de documento',
        validators=[
            validators.RegexValidator(
                #'^[0-9]{8,11}$',
                '^[0-9]{11}$',
                message='Ingrese un número de documento válido.'
            ),
        ]
    )

    tipo_documento = models.ForeignKey(
        TipoDocProveedor,
        verbose_name='Tipo de documento',
        on_delete=models.PROTECT,
    )

    razon_social = models.CharField (
        max_length=128,
        verbose_name='Razón social',
        help_text='Nombre o razón social de la persona o empresa',
        validators=[
            validators.RegexValidator(
                '^[a-zA-Z0-9áéíóúñÁÉÍÓÚÑ., \-]+$',
                message='Ingrese una razón social válida.'
            ),
        ]
    )

    direccion = models.CharField(
        max_length=170,
        verbose_name='Dirección',
        help_text='Dirección de la persona o empresa',
        validators=[
            validators.RegexValidator(
                '^[a-zA-Z0-9áéíóúñÁÉÍÓÚÑ., \-]+$',
                message='Ingrese una dirección válida.'
            ),
        ]
    )

    _verificacion_obj = models.CharField(max_length=1, choices=_VERIFICACION_OBJ, default='N')
    _estado_obj = models.CharField(max_length=1, choices=_ESTADO_OBJ, default='A')
    _creado = models.DateTimeField(auto_now_add=True,)
    _modificado = models.DateTimeField(auto_now=True,)

    def clean(self, *args, **kwargs):
        # try:
        #     if self.tipo_documento.pk == 'RUC':
        #         if len(self.id) != 11:
        #             raise validators.ValidationError('Número de documento RUC debe tener 11 dígitos.')
        #     elif self.tipo_documento.pk == 'DNI':
        #         if len(self.id) != 8:
        #             raise validators.ValidationError('Número de documento DNI debe tener 8 dígitos.')
        #     elif self.tipo_documento.pk == 'NIT': #NIT
        #         if len(self.id) != 10:
        #             raise validators.ValidationError("Número de documento NIT debe tener 10 dígitos.")
        # except ObjectDoesNotExist:
        #     pass
        super(Proveedor, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.razon_social = ' '.join(self.razon_social.upper().split())
        self.direccion = ' '.join(self.direccion.upper().split())
        self._verificacion_obj = 'N'
        super(Proveedor, self).save(*args, **kwargs)

    def __str__(self):
        return ('%s (%s %s)' % (self.razon_social, self.tipo_documento, self.id))

    class Meta:
        unique_together = ( ('razon_social',), )
        verbose_name = ('proveedor')
        verbose_name_plural = ('proveedores')