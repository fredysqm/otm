from django.contrib import admin
from reversion.admin import VersionAdmin
from core.models import Pais


@admin.register(Pais)
class PaisAdmin(VersionAdmin):
    list_display = ('id', 'nombre', '_creado','_modificado',)
    exclude = ()
    search_fields = ('id', 'nombre',)
    #list_filter = ('creado','acceso', 'estado')
    ordering = ['id']
    #actions = (slink_activar_action, slink_deshabilitar_action,)


# class ProveedorAdmin(admin.ModelAdmin):
#     list_display = ('id', 'razon_social', 'tipo_documento', 'nro_documento', 'direccion',)
#     exclude = ('_fts','_creado','_modificado',)
#     search_fields = ('id', '@_fts',)
#     #list_filter = ('creado','acceso', 'estado')
#     #ordering = ['-id']
#     #actions = (slink_activar_action, slink_deshabilitar_action,)


# class TipoDocProveedorAdmin(admin.ModelAdmin):
#     list_display = ('siglas', 'nombre',)
#     search_fields = ('siglas', 'nombre',)
#     ordering = ['siglas']


# admin.site.register(Proveedor, ProveedorAdmin)
# admin.site.register(TipoDocProveedor, TipoDocProveedorAdmin)