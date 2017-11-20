from django.contrib import admin
from core.models import Proveedor, TipoDocProveedor
from reversion.admin import VersionAdmin


class ProveedorAdmin(VersionAdmin):
    list_display = ('id', 'razon_social', 'tipo_documento', 'nro_documento', 'direccion',)
    exclude = ('_fts','_creado','_modificado',)
    search_fields = ('id', '@_fts',)
    #list_filter = ('creado','acceso', 'estado')
    #ordering = ['-id']
    #actions = (slink_activar_action, slink_deshabilitar_action,)


class TipoDocProveedorAdmin(VersionAdmin):
    list_display = ('id', 'siglas', 'nombre',)
    search_fields = ('id', 'siglas', 'nombre',)
    ordering = ['id']


admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(TipoDocProveedor, TipoDocProveedorAdmin)