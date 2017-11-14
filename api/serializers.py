from rest_framework import serializers
from mantenimiento.models import Proveedor, TipoDocProveedor


class ProveedorSerializer(serializers.ModelSerializer):

    #tipo_documento = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Proveedor
        fields = ('id', 'razon_social','tipo_documento','nro_documento','direccion', '_creado', '_modificado')
        depth = 2