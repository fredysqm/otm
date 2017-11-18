from rest_framework import serializers
from mantenimiento.models import Proveedor, TipoDocProveedor


class ProveedorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Proveedor
        fields = ('id', 'razon_social','tipo_documento','nro_documento','direccion', '_creado', '_modificado')
        #depth = 2