from rest_framework import serializers
from core.models import *


class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = ('id', 'nombre', 'creado', 'modificado',)

class CiudadSerializer(serializers.ModelSerializer):
    pais__nombre = serializers.ReadOnlyField()
    class Meta:
        model = Ciudad
        fields = ('id', 'nombre', 'pais', 'pais__nombre', 'creado', 'modificado',)

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
    ciudad__nombre = serializers.ReadOnlyField()
    pais__nombre = serializers.ReadOnlyField()

    class Meta:
        model = Localidad
        fields = ('id', 'nombre', 'ciudad', 'ciudad__nombre', 'pais__nombre', 'altitud', 'creado', 'modificado')

class MarcaComercialSerializer(serializers.ModelSerializer):
    proveedor__razon_social = serializers.ReadOnlyField()
    categoria_servicio__nombre = serializers.ReadOnlyField()
    localidad__nombre = serializers.ReadOnlyField()
    modalidad_pago__nombre = serializers.ReadOnlyField()

    class Meta:
        model = MarcaComercial
        fields = ('id', 'nombre', 'proveedor', 'proveedor__razon_social', 'categoria_servicio', 'categoria_servicio__nombre', 'localidad', 'localidad__nombre', 'modalidad_pago', 'modalidad_pago__nombre', 'direccion', 'telefono_fijo', 'telefono_movil', 'central_reservas', 'email', 'sitio_web', 'observaciones', 'creado', 'modificado')

class TipoCuentaBancoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoCuentaBanco
        fields = ('id', 'nombre', 'creado', 'modificado')

class MarcaComercialCuentaSerializer(serializers.ModelSerializer):
    marca_comercial__nombre = serializers.ReadOnlyField()
    banco__nombre = serializers.ReadOnlyField()
    moneda__nombre = serializers.ReadOnlyField()
    tipo_cuenta__nombre = serializers.ReadOnlyField()

    class Meta:
        model = MarcaComercialCuenta
        fields = ('id', 'marca_comercial', 'marca_comercial__nombre', 'banco', 'banco__nombre', 'moneda', 'moneda__nombre', 'tipo_cuenta', 'tipo_cuenta__nombre', 'titular', 'cta', 'cci', 'creado', 'modificado')