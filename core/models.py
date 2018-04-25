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
        return ('%s (%s)' % (self.nombre, self.id))

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
        return ('%s (%s)' % (self.nombre, self.id))

    class Meta:
        unique_together = ( ('nombre',), )
        verbose_name = ('idioma')
        verbose_name_plural = ('idiomas')


class Moneda(models.Model):
    id = models.CharField (
        primary_key=True,
        max_length=3,
        verbose_name='Siglas',
        help_text='Siglas de la moneda',
        validators=[
            validators.RegexValidator(
                '^[a-zA-Z0-9]{3}$',
                message='Ingrese siglas válidas.'
            ),
        ]
    )
    
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
        self.id = ' '.join(self.id.upper().split())
        self.nombre = ' '.join(self.nombre.upper().split())
        self.simbolo = ' '.join(self.simbolo.upper().split())
        super(Moneda, self).save(*args, **kwargs)

    def __str__(self):
        return ('%s (%s)' % (self.nombre, self.simbolo))

    class Meta:
        unique_together = ( ('nombre',), )
        verbose_name = ('moneda')
        verbose_name_plural = ('monedas')


class Banco(models.Model):
    id = models.CharField (
        primary_key=True,
        max_length=3,
        verbose_name='Siglas',
        help_text='Siglas del banco',
        validators=[
            validators.RegexValidator(
                '^[a-zA-Z0-9]{3}$',
                message='Ingrese siglas válidas.'
            ),
        ]
    )

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
        self.id = ' '.join(self.id.upper().split())
        self.nombre = ' '.join(self.nombre.upper().split())
        super(Banco, self).save(*args, **kwargs)

    def __str__(self):
        return ('%s (%s)' % (self.nombre, self.id))

    class Meta:
        unique_together = ( ('nombre',), )
        verbose_name = ('banco')
        verbose_name_plural = ('bancos')


class Operador(models.Model):
    id = models.CharField (
        primary_key=True,
        verbose_name='Siglas',
        max_length=6,
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
        return ('%s (%s)' % (self.nombre, self.id))

    class Meta:
        unique_together = ( ('nombre',), )
        verbose_name = ('operador')
        verbose_name_plural = ('operadores')


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
        return ('%s (%s)' % (self.nombre, self.id))

    class Meta:
        unique_together = ( ('nombre',), )
        verbose_name = ('tipo de documento proveedor')
        verbose_name_plural = ('tipos de documento proveedor')


class ModalidadPago(models.Model):
    id = models.CharField (
        primary_key=True,
        max_length=3,
        verbose_name='Siglas',
        help_text='Siglas de la modalidad de pago',
        validators=[
            validators.RegexValidator(
                '^[a-zA-Z0-9]{3}$',
                message='Ingrese siglas válidas.'
            ),
        ]
    )

    nombre = models.CharField (
        max_length=50,
        verbose_name='Nombre',
        help_text='Nombre de la modalidad de pago',
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
        super(ModalidadPago, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.id = ' '.join(self.id.upper().split())
        self.nombre = ' '.join(self.nombre.upper().split())
        super(ModalidadPago, self).save(*args, **kwargs)

    def __str__(self):
        return ('%s' % (self.id,))

    class Meta:
        unique_together = ( ('nombre',), )
        verbose_name = ('modalidad de pago')
        verbose_name_plural = ('modalidades de pago')


class CategoriaServicio(models.Model):
    id = models.CharField (
        primary_key=True,
        max_length=3,
        verbose_name='Siglas',
        help_text='Siglas de la categoría de servicio',
        validators=[
            validators.RegexValidator(
                '^[a-zA-Z0-9]{3}$',
                message='Ingrese siglas válidas.'
            ),
        ]
    )

    nombre = models.CharField (
        max_length=50,
        verbose_name='Nombre',
        help_text='Nombre de la categoría de servicio',
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
        super(CategoriaServicio, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.id = ' '.join(self.id.upper().split())
        self.nombre = ' '.join(self.nombre.upper().split())
        super(CategoriaServicio, self).save(*args, **kwargs)

    def __str__(self):
        return ('%s (%s)' % (self.nombre, self.id))

    class Meta:
        unique_together = ( ('nombre',), )
        verbose_name = ('categoría de servicio')
        verbose_name_plural = ('categorías de servicio')


class Proveedor(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=11,
        verbose_name='Número de documento',
        validators=[
            validators.RegexValidator(
                #'^[0-9]{8,11}$',
                '^[1-2]{1}[0-9]{10}$', #Solo para RUC
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

    domicilio = models.CharField(
        max_length=170,
        verbose_name='Domicilio',
        help_text='Domicilio de la persona o empresa',
        validators=[
            validators.RegexValidator(
                '^[a-zA-Z0-9áéíóúñÁÉÍÓÚÑ., \-]+$',
                message='Ingrese un domicilio válido.'
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
        self.domicilio = ' '.join(self.domicilio.upper().split())
        self._verificacion_obj = 'N'
        super(Proveedor, self).save(*args, **kwargs)

    def __str__(self):
        return ('%s (%s %s)' % (self.razon_social, self.tipo_documento, self.id))

    class Meta:
        unique_together = ( ('razon_social',), )
        verbose_name = ('proveedor')
        verbose_name_plural = ('proveedores')


class Localidad(models.Model):
    nombre = models.CharField (
        max_length=100,
        verbose_name='Nombre',
        help_text='Nombre de la localidad',
        validators=[
            validators.RegexValidator(
                '^[a-zA-Z0-9áéíóúñÁÉÍÓÚÑ., \-]+$',
                message='Ingrese un nombre válido.'
            ),
        ]
    )

    ciudad = models.ForeignKey (
        Ciudad,
        on_delete=models.PROTECT,
    )

    altitud = models.PositiveIntegerField(
        default=0,
        verbose_name='Altitud',
        help_text='Altitud de la localidad m.s.n.m.',
    )

    _estado_obj = models.CharField(max_length=1, choices=_ESTADO_OBJ, default='A')
    _creado = models.DateTimeField(auto_now_add=True,)
    _modificado = models.DateTimeField(auto_now=True,)

    def clean(self, *args, **kwargs):
        super(Localidad, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.nombre = ' '.join(self.nombre.upper().split())
        super(Localidad, self).save(*args, **kwargs)

    def __str__(self):
        return ('%s (%s)' % (self.nombre, self.ciudad.pk))

    class Meta:
        unique_together = ( ('nombre', 'ciudad'), )
        verbose_name = ('localidad')
        verbose_name_plural = ('localidades')


class MarcaComercial(models.Model):
    nombre = models.CharField (
        max_length=100,
        verbose_name='Nombre',
        help_text='Nombre de la marca comercial',
        validators=[
            validators.RegexValidator(
                '^[a-zA-Z0-9áéíóúñÁÉÍÓÚÑ., \-]+$',
                message='Ingrese un nombre válido.'
            ),
        ]
    )

    proveedor = models.ForeignKey (
        Proveedor,
        on_delete=models.PROTECT,
    )

    categoria_servicio = models.ForeignKey (
        CategoriaServicio,
        on_delete=models.PROTECT,
    )

    localidad = models.ForeignKey (
        Localidad,
        on_delete=models.PROTECT,
    )

    modalidad_pago = models.ForeignKey (
        ModalidadPago,
        on_delete=models.PROTECT,
    )

    direccion = models.CharField(
        max_length=170,
        blank=True,
        verbose_name='Dirección',
        help_text='Dirección de la marca comercial',
        validators=[
            validators.RegexValidator(
                '^[a-zA-Z0-9áéíóúñÁÉÍÓÚÑ., \-]+$',
                message='Ingrese una dirección válida.'
            ),
        ]
    )

    telefono_fijo = models.CharField(
        max_length=12,
        blank=True,
        verbose_name='Teléfono fijo',
        help_text='Ingrese solo números',
        validators=[
            validators.RegexValidator(
                '^[0-9]{6,}$',
                message='Ingrese un número de teléfono fijo válido.'
            ),
        ]
    )

    telefono_movil = models.CharField(
        max_length=12,
        blank=True,
        verbose_name='Teléfono móvil',
        help_text='Ingrese solo números',
        validators=[
            validators.RegexValidator(
                '^[0-9]{9,}$',
                message='Ingrese un número de teléfono móvil válido.'
            ),
        ]
    )

    email = models.EmailField(
        max_length=128,
        blank=True,
        verbose_name='Email',
    )

    sitio_web = models.URLField(
        max_length=128,
        blank=True,
        verbose_name='Sitio Web',
    )

    observaciones = models.CharField(
        max_length=512,
        blank=True,
        verbose_name='Observaciones',
    )

    _verificacion_obj = models.CharField(max_length=1, choices=_VERIFICACION_OBJ, default='N')
    _estado_obj = models.CharField(max_length=1, choices=_ESTADO_OBJ, default='A')
    _creado = models.DateTimeField(auto_now_add=True,)
    _modificado = models.DateTimeField(auto_now=True,)

    def clean(self, *args, **kwargs):
        super(MarcaComercial, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.nombre = ' '.join(self.nombre.upper().split())
        self.direccion = ' '.join(self.direccion.upper().split())
        self.telefono_fijo = ' '.join(self.telefono_fijo.upper().split())
        self.telefono_movil = ' '.join(self.telefono_movil.upper().split())
        self.email = ' '.join(self.email.lower().split())
        self.sitio_web = ' '.join(self.sitio_web.lower().split())
        self.observaciones = self.observaciones.strip()
        super(MarcaComercial, self).save(*args, **kwargs)

    def __str__(self):
        return ('%s (%s)' % (self.nombre, self.proveedor.pk))

    class Meta:
        unique_together = ( ('nombre', 'proveedor'), )
        verbose_name = ('marca comecial')
        verbose_name_plural = ('marcas comerciales')


class TipoCuentaBanco(models.Model):
    id = models.CharField (
        primary_key=True,
        max_length=3,
        verbose_name='Siglas',
        help_text='Siglas del tipo de cuenta de banco',
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
        help_text='Nombre del tipo de cuenta de banco',
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
        super(TipoCuentaBanco, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.id = ' '.join(self.id.upper().split())
        self.nombre = ' '.join(self.nombre.upper().split())
        super(TipoCuentaBanco, self).save(*args, **kwargs)

    def __str__(self):
        return ('%s (%s)' % (self.nombre, self.id))

    class Meta:
        unique_together = ( ('nombre',), )
        verbose_name = ('tipo de cuenta banco')
        verbose_name_plural = ('tipos de cuenta banco')


class MarcaComercialCuenta(models.Model):
    marca_comercial = models.ForeignKey (
        MarcaComercial,
        on_delete=models.PROTECT,
    )

    banco = models.ForeignKey (
        Banco,
        on_delete=models.PROTECT,
    )

    moneda = models.ForeignKey (
        Moneda,
        on_delete=models.PROTECT,
    )

    tipo_cuenta = models.ForeignKey (
        TipoCuentaBanco,
        on_delete=models.PROTECT,
    )

    titular = models.CharField (
        max_length=128,
        verbose_name='Razón social',
        help_text='Nombre del titular de la cuenta',
        validators=[
            validators.RegexValidator(
                '^[a-zA-Z0-9áéíóúñÁÉÍÓÚÑ., \-]+$',
                message='Ingrese un nombre válida.'
            ),
        ]
    )

    cta = models.CharField(
        max_length=30,
        verbose_name='Número de cuenta',
        validators=[
            validators.RegexValidator(
                '^[0-9]$',
                message='Ingrese un número de cuenta válido.'
            ),
        ]
    )

    cci = models.CharField(
        max_length=40,
        blank=True,
        verbose_name='Número de cci',
        validators=[
            validators.RegexValidator(
                '^[0-9]$',
                message='Ingrese un número de cci válido.'
            ),
        ]
    )

    _verificacion_obj = models.CharField(max_length=1, choices=_VERIFICACION_OBJ, default='N')
    _estado_obj = models.CharField(max_length=1, choices=_ESTADO_OBJ, default='A')
    _creado = models.DateTimeField(auto_now_add=True,)
    _modificado = models.DateTimeField(auto_now=True,)

    def clean(self, *args, **kwargs):
        super(MarcaComercialCuenta, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.titular = ' '.join(self.titular.upper().split())
        self.cta = ' '.join(self.cta.upper().split())
        self.cci = ' '.join(self.cci.upper().split())
        super(MarcaComercialCuenta, self).save(*args, **kwargs)

    def __str__(self):
        return ('%s (%s)' % (self.titular, self.cta))

    class Meta:
        unique_together = ( ('marca_comercial', 'cta'), ('marca_comercial', 'moneda'), )
        verbose_name = ('marca comecial cuenta')
        verbose_name_plural = ('marcas comerciales cuentas')