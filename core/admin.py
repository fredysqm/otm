from django.contrib import admin
from reversion.admin import VersionAdmin
from core.models import *


#Actions
def generic_activar_estado_obj_action(modeladmin, request, queryset):
    queryset.update(estado_obj='A')
def generic_suspender_estado_obj_action(modeladmin, request, queryset):
    queryset.update(estado_obj='S')
generic_activar_estado_obj_action.short_description = "Activar item(s) seleccionado(s)"
generic_suspender_estado_obj_action.short_description = "Suspender item(s) seleccionado(s)"


#ModelAdmin
@admin.register(Pais)
class PaisAdmin(VersionAdmin):
    list_display = ('id', 'nombre', 'activo', 'creado', 'modificado',)
    search_fields = ('id', 'nombre',)
    list_filter = ( 'estado_obj', 'creado', 'modificado' )
    ordering = ['nombre']
    actions = (generic_activar_estado_obj_action, generic_suspender_estado_obj_action,)
    def activo(self, obj):
        return obj.estado_obj == 'A'
    activo.boolean = True

@admin.register(Ciudad)
class CiudadAdmin(VersionAdmin):
    list_display = ('id', 'pais', 'nombre', 'activo', 'creado','modificado',)
    list_select_related = ('pais', )
    #raw_id_fields = ('pais',)
    search_fields = ('id', 'pais__nombre', 'pais__id', 'nombre',)
    list_filter = ( ('pais', admin.RelatedOnlyFieldListFilter), 'estado_obj', 'creado', 'modificado' )
    ordering = ['id']
    actions = (generic_activar_estado_obj_action, generic_suspender_estado_obj_action,)
    def activo(self, obj):
        return obj.estado_obj == 'A'
    activo.boolean = True

@admin.register(Idioma)
class IdiomaAdmin(VersionAdmin):
    list_display = ('id', 'nombre', 'activo', 'creado','modificado',)
    search_fields = ('id', 'nombre',)
    list_filter = ( 'estado_obj', 'creado', 'modificado' )
    ordering = ['id']
    actions = (generic_activar_estado_obj_action, generic_suspender_estado_obj_action,)
    def activo(self, obj):
        return obj.estado_obj == 'A'
    activo.boolean = True

@admin.register(Moneda)
class MonedaAdmin(VersionAdmin):
    list_display = ('id', 'nombre', 'simbolo', 'activo', 'creado','modificado',)
    search_fields = ('id', 'nombre',)
    list_filter = ( 'estado_obj', 'creado', 'modificado' )
    ordering = ['id']
    actions = (generic_activar_estado_obj_action, generic_suspender_estado_obj_action,)
    def activo(self, obj):
        return obj.estado_obj == 'A'
    activo.boolean = True

@admin.register(Banco)
class BancoaAdmin(VersionAdmin):
    list_display = ('id', 'nombre', 'activo', 'creado','modificado',)
    search_fields = ('id', 'nombre',)
    list_filter = ( 'estado_obj', 'creado', 'modificado' )
    ordering = ['id']
    actions = (generic_activar_estado_obj_action, generic_suspender_estado_obj_action,)
    def activo(self, obj):
        return obj.estado_obj == 'A'
    activo.boolean = True

@admin.register(Operador)
class OperadorAdmin(VersionAdmin):
    list_display = ('id', 'nombre', 'activo', 'creado','modificado',)
    search_fields = ('id', 'nombre',)
    list_filter = ( 'estado_obj', 'creado', 'modificado' )
    ordering = ['id']
    actions = (generic_activar_estado_obj_action, generic_suspender_estado_obj_action,)
    def activo(self, obj):
        return obj.estado_obj == 'A'
    activo.boolean = True

@admin.register(TipoDocProveedor)
class TipoDocProveedorAdmin(VersionAdmin):
    list_display = ('id', 'nombre', 'activo', 'creado','modificado',)
    search_fields = ('id', 'nombre',)
    list_filter = ( 'estado_obj', 'creado', 'modificado' )
    ordering = ['id']
    actions = (generic_activar_estado_obj_action, generic_suspender_estado_obj_action,)
    def activo(self, obj):
        return obj.estado_obj == 'A'
    activo.boolean = True

@admin.register(ModalidadPago)
class ModalidadPagoAdmin(VersionAdmin):
    list_display = ('id', 'nombre', 'activo', 'creado','modificado',)
    search_fields = ('id', 'nombre',)
    list_filter = ( 'estado_obj', 'creado', 'modificado' )
    ordering = ['id']
    actions = (generic_activar_estado_obj_action, generic_suspender_estado_obj_action,)
    def activo(self, obj):
        return obj.estado_obj == 'A'
    activo.boolean = True

@admin.register(CategoriaServicio)
class CategoriaServicioAdmin(VersionAdmin):
    list_display = ('id', 'nombre', 'activo', 'creado','modificado',)
    search_fields = ('id', 'nombre',)
    list_filter = ( 'estado_obj', 'creado', 'modificado' )
    ordering = ['id']
    actions = (generic_activar_estado_obj_action, generic_suspender_estado_obj_action,) 
    def activo(self, obj):
        return obj.estado_obj == 'A'
    activo.boolean = True

@admin.register(Proveedor)
class ProveedorAdmin(VersionAdmin):
    list_display = ('id', 'razon_social', 'activo', 'creado','modificado',)
    list_display_links = ('id',)
    #exclude = ('_fts',)
    search_fields = ('razon_social',)
    list_filter = ( 'estado_obj', 'creado', 'modificado' )
    ordering = ['id']
    actions = (generic_activar_estado_obj_action, generic_suspender_estado_obj_action)
    def activo(self, obj):
        return obj.estado_obj == 'A'
    activo.boolean = True

@admin.register(Localidad)
class LocalidadAdmin(VersionAdmin):
    list_display = ('id', 'nombre', 'altitud', 'activo', 'creado','modificado',)
    search_fields = ('id', 'nombre',)
    list_filter = ( 'estado_obj', 'creado', 'modificado' )
    ordering = ['id']
    actions = (generic_activar_estado_obj_action, generic_suspender_estado_obj_action,)
    def activo(self, obj):
        return obj.estado_obj == 'A'
    activo.boolean = True

@admin.register(MarcaComercial)
class MarcaComercialAdmin(VersionAdmin):
    list_display = ('id', 'nombre', 'proveedor', 'activo', 'creado','modificado',)
    search_fields = ('id', 'nombre',)
    list_filter = ( 'estado_obj', 'creado', 'modificado' )
    ordering = ['id']
    actions = (generic_activar_estado_obj_action, generic_suspender_estado_obj_action,)
    def activo(self, obj):
        return obj.estado_obj == 'A'
    activo.boolean = True

@admin.register(TipoCuentaBanco)
class TipoCuentaBancoAdmin(VersionAdmin):
    list_display = ('id', 'nombre',  'activo', 'creado','modificado',)
    search_fields = ('id', 'nombre',)
    list_filter = ( 'estado_obj', 'creado', 'modificado' )
    ordering = ['id']
    actions = (generic_activar_estado_obj_action, generic_suspender_estado_obj_action,)
    def activo(self, obj):
        return obj.estado_obj == 'A'
    activo.boolean = True

@admin.register(MarcaComercialCuenta)
class MarcaComercialCuentaAdmin(VersionAdmin):
    list_display = ('id', 'titular', 'cta', 'activo', 'creado','modificado',)
    search_fields = ('id', 'nombre',)
    list_filter = ( 'estado_obj', 'creado', 'modificado' )
    ordering = ['id']
    actions = (generic_activar_estado_obj_action, generic_suspender_estado_obj_action,)
    def activo(self, obj):
        return obj.estado_obj == 'A'
    activo.boolean = True