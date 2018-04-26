from rest_framework import serializers
from core.models import *


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

class OperadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operador
        fields = ('id', 'nombre', '_creado', '_modificado')

class TipoDocProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDocProveedor
        fields = ('id', 'nombre', '_creado', '_modificado')

class ModalidadPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModalidadPago
        fields = ('id', 'nombre', '_creado', '_modificado')

class CategoriaServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaServicio
        fields = ('id', 'nombre', '_creado', '_modificado')

class ProveedorSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        instance = Proveedor(**attrs)
        instance.clean()
        return attrs

    class Meta:
        model = Proveedor
        fields = ('id', 'tipo_documento', 'razon_social', 'direccion', '_creado', '_modificado')
        #depth = 2