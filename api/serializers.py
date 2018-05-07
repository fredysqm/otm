from rest_framework import serializers
from core.models import *


class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = ('id', 'nombre', 'creado', 'modificado')

class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = ('id', 'pais', 'nombre', 'creado', 'modificado')
        depth = 2

class IdiomaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idioma
        fields = ('id', 'nombre', 'creado', 'modificado')

class MonedaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moneda
        fields = ('id', 'nombre', 'simbolo', 'creado', 'modificado')

class BancoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banco
        fields = ('id', 'nombre', 'creado', 'modificado')

class OperadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operador
        fields = ('id', 'nombre', 'creado', 'modificado')

class TipoDocProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDocProveedor
        fields = ('id', 'nombre', 'creado', 'modificado')

class ModalidadPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModalidadPago
        fields = ('id', 'nombre', 'creado', 'modificado')

class CategoriaServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaServicio
        fields = ('id', 'nombre', 'creado', 'modificado')

class ProveedorSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        instance = Proveedor(**attrs)
        instance.clean()
        return attrs

    class Meta:
        model = Proveedor
        fields = ('id', 'tipo_documento', 'razon_social', 'creado', 'modificado')
        #depth = 2

class LocalidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localidad
        fields = ('id', 'nombre', 'ciudad', 'altitud', 'creado', 'modificado')
        #depth = 2

class MarcaComercialSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarcaComercial
        fields = ('id', 'nombre', 'proveedor', 'categoria_servicio', 'localidad', 'modalidad_pago', 'direccion', 'telefono_fijo', 'telefono_movil',
                    'email', 'sitio_web', 'observaciones', 'creado', 'modificado')
        #depth = 2

class TipoCuentaBancoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoCuentaBanco
        fields = ('id', 'nombre', 'creado', 'modificado')

class MarcaComercialCuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarcaComercialCuenta
        fields = ('id', 'marca_comercial', 'banco', 'moneda', 'tipo_cuenta', 'titular', 'cta', 'cci', 'creado', 'modificado')