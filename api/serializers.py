from rest_framework import serializers
from core.models import Pais, Ciudad, Idioma, Moneda, Banco


class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = ('id', 'nombre', '_creado', '_modificado')

class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = ('id', 'pais', 'nombre', '_creado', '_modificado')
        depth = 2

class IdiomaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idioma
        fields = ('id', 'nombre', '_creado', '_modificado')

class MonedaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moneda
        fields = ('id', 'nombre', 'simbolo', '_creado', '_modificado')

class BancoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banco
        fields = ('id', 'nombre', '_creado', '_modificado')

# class ProveedorSerializer(serializers.ModelSerializer):

#     def validate(self, attrs):
#         instance = Proveedor(**attrs)
#         instance.clean()
#         return attrs

#     class Meta:
#         model = Proveedor
#         fields = ('id', 'tipo_documento', 'razon_social', 'direccion', '_creado', '_modificado')
#         #depth = 2