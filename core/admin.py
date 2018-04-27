from django.contrib import admin
from reversion.admin import VersionAdmin
from core.models import *


#Actions
def generic_activar_estado_obj_action(modeladmin, request, queryset):
    queryset.update(_estado_obj='A')
def generic_suspender_estado_obj_action(modeladmin, request, queryset):
    queryset.update(_estado_obj='S')
generic_activar_estado_obj_action.short_description = "Activar item(s) seleccionado(s)"
generic_suspender_estado_obj_action.short_description = "Suspender item(s) seleccionado(s)"

def generic_verificar_obj_action(modeladmin, request, queryset):
    queryset.update(_verificacion_obj='S')
generic_verificar_obj_action.short_description = "Verificar item(s) seleccionado(s)"


#ModelAdmin
@admin.register(Pais)
class PaisAdmin(VersionAdmin):
    list_display = ('id', 'nombre', '_activo', '_creado','_modificado',)
    search_fields = ('id', 'nombre',)
    list_filter = ( '_estado_obj', '_creado', '_modificado' )
    ordering = ['nombre']
    actions = (generic_activar_estado_obj_action, generic_suspender_estado_obj_action,)
    def _activo(self, obj):
        return obj._estado_obj == 'A'
    _activo.boolean = True

@admin.register(Ciudad)
class CiudadAdmin(VersionAdmin):
    list_display = ('id', 'pais', 'nombre', '_activo', '_creado','_modificado',)
    list_select_related = ('pais', )
    #raw_id_fields = ('pais',)
    search_fields = ('id', 'pais__nombre', 'pais__id', 'nombre',)
    list_filter = ( ('pais', admin.RelatedOnlyFieldListFilter), '_estado_obj', '_creado', '_modificado' )
    ordering = ['id']
    actions = (generic_activar_estado_obj_action, generic_suspender_estado_obj_action,)
    def _activo(self, obj):
        return obj._estado_obj == 'A'
    _activo.boolean = True

@admin.register(Idioma)
class IdiomaAdmin(VersionAdmin):
    list_display = ('id', 'nombre', '_activo', '_creado','_modificado',)
    search_fields = ('id', 'nombre',)
    list_filter = ( '_estado_obj', '_creado', '_modificado' )
    ordering = ['id']
    actions = (generic_activar_estado_obj_action, generic_suspender_estado_obj_action,)
    def _activo(self, obj):
        return obj._estado_obj == 'A'
    _activo.boolean = True

@admin.register(Moneda)
class MonedaAdmin(VersionAdmin):
    list_display = ('id', 'nombre', 'simbolo', '_activo', '_creado','_modificado',)
    search_fields = ('id', 'nombre',)
    list_filter = ( '_estado_obj', '_creado', '_modificado' )
    ordering = ['id']
    actions = (generic_activar_estado_obj_action, generic_suspender_estado_obj_action,)
    def _activo(self, obj):
        return obj._estado_obj == 'A'
    _activo.boolean = True

@admin.register(Banco)
class BancoaAdmin(VersionAdmin):
    list_display = ('id', 'nombre', '_activo', '_creado','_modificado',)
    search_fields = ('id', 'nombre',)
    list_filter = ( '_estado_obj', '_creado', '_modificado' )
    ordering = ['id']
    actions = (generic_activar_estado_obj_action, generic_suspender_estado_obj_action,)
    def _activo(self, obj):
        return obj._estado_obj == 'A'
    _activo.boolean = True

@admin.register(Operador)
class OperadorAdmin(VersionAdmin):
    list_display = ('id', 'nombre', '_activo', '_creado','_modificado',)
    search_fields = ('id', 'nombre',)
    list_filter = ( '_estado_obj', '_creado', '_modificado' )
    ordering = ['id']
    actions = (generic_activar_estado_obj_action, generic_suspender_estado_obj_action,)
    def _activo(self, obj):
        return obj._estado_obj == 'A'
    _activo.boolean = True

@admin.register(TipoDocProveedor)
class TipoDocProveedorAdmin(VersionAdmin):
    list_display = ('id', 'nombre', '_activo', '_creado','_modificado',)
    search_fields = ('id', 'nombre',)
    list_filter = ( '_estado_obj', '_creado', '_modificado' )
    ordering = ['id']
    actions = (generic_activar_estado_obj_action, generic_suspender_estado_obj_action,)
    def _activo(self, obj):
        return obj._estado_obj == 'A'
    _activo.boolean = True

@admin.register(ModalidadPago)
class ModalidadPagoAdmin(VersionAdmin):
    list_display = ('id', 'nombre', '_activo', '_creado','_modificado',)
    search_fields = ('id', 'nombre',)
    list_filter = ( '_estado_obj', '_creado', '_modificado' )
    ordering = ['id']
    actions = (generic_activar_estado_obj_action, generic_suspender_estado_obj_action,)
    def _activo(self, obj):
        return obj._estado_obj == 'A'
    _activo.boolean = True

@admin.register(CategoriaServicio)
class CategoriaServicioAdmin(VersionAdmin):
    list_display = ('id', 'nombre', '_activo', '_creado','_modificado',)
    search_fields = ('id', 'nombre',)
    list_filter = ( '_estado_obj', '_creado', '_modificado' )
    ordering = ['id']
    actions = (generic_activar_estado_obj_action, generic_suspender_estado_obj_action,) 
    def _activo(self, obj):
        return obj._estado_obj == 'A'
    _activo.boolean = True

@admin.register(Proveedor)
class ProveedorAdmin(VersionAdmin):
    list_display = ('tipo_documento', 'id', 'razon_social', '_verificado', '_activo', '_creado','_modificado',)
    list_display_links = ('id',)
    #exclude = ('_fts',)
    search_fields = ('razon_social',)
    list_filter = ( '_verificacion_obj',  '_estado_obj', '_creado', '_modificado' )
    ordering = ['id']
    actions = (generic_activar_estado_obj_action, generic_suspender_estado_obj_action, generic_verificar_obj_action)
    def _activo(self, obj):
        return obj._estado_obj == 'A'
    _activo.boolean = True
    def _verificado(self, obj):
        return obj._verificacion_obj == 'S'
    _verificado.boolean = True

@admin.register(Localidad)
class LocalidadAdmin(VersionAdmin):
    list_display = ('id', 'nombre', 'altitud', '_activo', '_creado','_modificado',)
    search_fields = ('id', 'nombre',)
    list_filter = ( '_estado_obj', '_creado', '_modificado' )
    ordering = ['id']
    actions = (generic_activar_estado_obj_action, generic_suspender_estado_obj_action,)
    def _activo(self, obj):
        return obj._estado_obj == 'A'
    _activo.boolean = True

@admin.register(MarcaComercial)
class MarcaComercialAdmin(VersionAdmin):
    list_display = ('id', 'nombre', 'proveedor', '_activo', '_creado','_modificado',)
    search_fields = ('id', 'nombre',)
    list_filter = ( '_estado_obj', '_creado', '_modificado' )
    ordering = ['id']
    actions = (generic_activar_estado_obj_action, generic_suspender_estado_obj_action,)
    def _activo(self, obj):
        return obj._estado_obj == 'A'
    _activo.boolean = True

@admin.register(TipoCuentaBanco)
class TipoCuentaBancoAdmin(VersionAdmin):
    list_display = ('id', 'nombre',  '_activo', '_creado','_modificado',)
    search_fields = ('id', 'nombre',)
    list_filter = ( '_estado_obj', '_creado', '_modificado' )
    ordering = ['id']
    actions = (generic_activar_estado_obj_action, generic_suspender_estado_obj_action,)
    def _activo(self, obj):
        return obj._estado_obj == 'A'
    _activo.boolean = True

@admin.register(MarcaComercialCuenta)
class MarcaComercialCuentaAdmin(VersionAdmin):
    list_display = ('id', 'titular', 'cta', '_activo', '_creado','_modificado',)
    search_fields = ('id', 'nombre',)
    list_filter = ( '_estado_obj', '_creado', '_modificado' )
    ordering = ['id']
    actions = (generic_activar_estado_obj_action, generic_suspender_estado_obj_action,)
    def _activo(self, obj):
        return obj._estado_obj == 'A'
    _activo.boolean = True