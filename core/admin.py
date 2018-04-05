from django.contrib import admin
from reversion.admin import VersionAdmin
from core.models import Pais, Ciudad, Idioma, Moneda, Banco, Operador, TipoDocProveedor, Proveedor


@admin.register(Pais)
class PaisAdmin(VersionAdmin):
    list_display = ('id', 'nombre', '_creado','_modificado',)
    search_fields = ('id', 'nombre',)
    list_filter = ( '_estado_obj', '_creado', '_modificado' )
    ordering = ['nombre']

@admin.register(Ciudad)
class CiudadAdmin(VersionAdmin):
    list_display = ('id', 'pais', 'nombre', '_creado','_modificado',)
    list_select_related = ('pais', )
    #raw_id_fields = ('pais',)
    search_fields = ('id', 'pais__nombre', 'pais__id', 'nombre',)
    list_filter = ( ('pais', admin.RelatedOnlyFieldListFilter), '_estado_obj', '_creado', '_modificado' )
    ordering = ['id']

@admin.register(Idioma)
class IdiomaAdmin(VersionAdmin):
    list_display = ('id', 'nombre', '_creado','_modificado',)
    search_fields = ('id', 'nombre',)
    list_filter = ( '_estado_obj', '_creado', '_modificado' )
    ordering = ['id']

@admin.register(Moneda)
class MonedaAdmin(VersionAdmin):
    list_display = ('id', 'nombre', 'simbolo', '_creado','_modificado',)
    search_fields = ('id', 'nombre',)
    list_filter = ( '_estado_obj', '_creado', '_modificado' )
    ordering = ['id']

@admin.register(Banco)
class BancoaAdmin(VersionAdmin):
    list_display = ('id', 'nombre', '_creado','_modificado',)
    search_fields = ('id', 'nombre',)
    list_filter = ( '_estado_obj', '_creado', '_modificado' )
    ordering = ['id']

@admin.register(Operador)
class OperadorAdmin(VersionAdmin):
    list_display = ('id', 'nombre', '_creado','_modificado',)
    search_fields = ('id', 'nombre',)
    list_filter = ( '_estado_obj', '_creado', '_modificado' )
    ordering = ['id']

@admin.register(TipoDocProveedor)
class TipoDocProveedorAdmin(VersionAdmin):
    list_display = ('id', 'nombre', '_creado','_modificado',)
    search_fields = ('id', 'nombre',)
    list_filter = ( '_estado_obj', '_creado', '_modificado' )
    ordering = ['id']

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('tipo_documento', 'id', 'razon_social', '_creado','_modificado',)
    exclude = ('_fts',)
    search_fields = ('razon_social',)
    list_filter = ( ('tipo_documento', admin.RelatedOnlyFieldListFilter), '_estado_obj', '_creado', '_modificado' )
    ordering = ['id']