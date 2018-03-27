from rest_framework import serializers
from core.models import Pais, Ciudad


class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = ('id', 'nombre', '_creado', '_modificado')

class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = ('id', 'pais', 'nombre', '_creado', '_modificado')
        depth = 2

# class ProveedorSerializer(serializers.ModelSerializer):

#     def validate(self, attrs):
#         instance = Proveedor(**attrs)
#         instance.clean()
#         return attrs

#     class Meta:
#         model = Proveedor
#         fields = ('id', 'tipo_documento', 'razon_social', 'direccion', '_creado', '_modificado')
#         #depth = 2