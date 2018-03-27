from django.contrib import admin
from reversion.admin import VersionAdmin
from core.models import Pais, Ciudad, Idioma, Moneda


@admin.register(Pais)
class PaisAdmin(VersionAdmin):
    list_display = ('id', 'nombre', '_creado','_modificado',)
    search_fields = ('id', 'nombre',)
    ordering = ['id']

@admin.register(Ciudad)
class CiudadAdmin(VersionAdmin):
    list_display = ('id', 'pais', 'nombre', '_creado','_modificado',)
    list_select_related = ('pais', )
    raw_id_fields = ('pais',)
    search_fields = ('id', 'pais__nombre', 'pais__id', 'nombre',)
    list_filter = ( ('pais', admin.RelatedOnlyFieldListFilter), )
    ordering = ['id']

@admin.register(Idioma)
class IdiomaAdmin(VersionAdmin):
    list_display = ('id', 'nombre', '_creado','_modificado',)
    search_fields = ('id', 'nombre',)
    ordering = ['id']

@admin.register(Moneda)
class MonedaAdmin(VersionAdmin):
    list_display = ('id', 'nombre', 'simbolo', '_creado','_modificado',)
    search_fields = ('id', 'nombre',)
    ordering = ['id']