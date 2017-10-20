from django.contrib import admin
from reservas.models import Reserva, ReservaDetalle


class ReservaDetalleInline(admin.TabularInline):
    model = ReservaDetalle

class ReservaAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion', 'fecha', 'creado','modificado')
    search_fields = ('id', 'descripcion',)
    inlines = (ReservaDetalleInline,)
    #list_filter = ('creado','acceso', 'estado')
    #ordering = ['-id']
    #actions = (slink_activar_action, slink_deshabilitar_action,)

admin.site.register(Reserva, ReservaAdmin)