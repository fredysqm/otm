from django.contrib import admin
from mantenimiento.models import Proveedor, TipoDocProveedor


class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'razon_social', 'tipo_documento', 'nro_documento', 'direccion',)
    search_fields = ('id', 'descripcion', 'nro_documento', 'direccion',)
    #list_filter = ('creado','acceso', 'estado')
    #ordering = ['-id']
    #actions = (slink_activar_action, slink_deshabilitar_action,)


class TipoDocProveedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'siglas', 'nombre',)
    search_fields = ('id', 'siglas', 'nombre',)
    ordering = ['id']


admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(TipoDocProveedor, TipoDocProveedorAdmin)