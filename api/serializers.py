from rest_framework import serializers
from mantenimiento.models import Proveedor, TipoDocProveedor


class ProveedorSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        instance = Proveedor(**attrs)
        instance.clean()
        return attrs
    class Meta:
        model = Proveedor
        fields = ('id', 'razon_social','tipo_documento','nro_documento','direccion', '_creado', '_modificado')
        #depth = 2

