from rest_framework import serializers
from mantenimiento.models import Proveedor


class ProveedorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Proveedor
        fields = ('id', 'razon_social','tipo_documento','nro_documento','direccion')