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
        validators=[
            validators.MinLengthValidator(
                1,
                message='Ingrese un símbolo válido.'
            ),
        ]
    )

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