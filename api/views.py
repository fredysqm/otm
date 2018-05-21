from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import pagination
from rest_framework import filters
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from core.models import *
from api.serializers import *


class DefaultPagination(pagination.PageNumberPagination):
    page_size_query_param = 'page_size'
    page_size = 10
    max_page_size = 100

class DefaultPermissions(permissions.DjangoModelPermissions):
    perms_map = {
        'OPTIONS': [],
        'HEAD': [],
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }


class PaisViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = PaisSerializer
    queryset = Pais.objects.filter(estado_obj='A')
    pagination_class = DefaultPagination
    permission_classes = (DefaultPermissions,)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    search_fields = ('id', 'nombre',)

class CiudadViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = CiudadSerializer
    queryset = Ciudad.objects.select_related('pais').filter(estado_obj='A')
    pagination_class = DefaultPagination
    permission_classes = (DefaultPermissions,)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    search_fields = ('id', 'pais__id', 'pais__nombre', 'nombre',)

class IdiomaViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = IdiomaSerializer
    queryset = Idioma.objects.filter(estado_obj='A')
    pagination_class = DefaultPagination
    permission_classes = (DefaultPermissions,)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    search_fields = ('id', 'nombre',)

class MonedaViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = MonedaSerializer
    queryset = Moneda.objects.filter(estado_obj='A')
    pagination_class = DefaultPagination
    permission_classes = (DefaultPermissions,)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    search_fields = ('id', 'nombre',)

class BancoViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = BancoSerializer
    queryset = Banco.objects.filter(estado_obj='A')
    pagination_class = DefaultPagination
    permission_classes = (DefaultPermissions,)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    search_fields = ('id', 'nombre',)

class OperadorViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = OperadorSerializer
    queryset = Operador.objects.filter(estado_obj='A')
    pagination_class = DefaultPagination
    permission_classes = (DefaultPermissions,)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    search_fields = ('id', 'nombre',)

class TipoDocProveedorViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = TipoDocProveedorSerializer
    queryset = TipoDocProveedor.objects.filter(estado_obj='A')
    pagination_class = DefaultPagination
    permission_classes = (DefaultPermissions,)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    search_fields = ('id', 'nombre',)

class ModalidadPagoViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ModalidadPagoSerializer
    queryset = ModalidadPago.objects.filter(estado_obj='A')
    pagination_class = DefaultPagination
    permission_classes = (DefaultPermissions,)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    search_fields = ('id', 'nombre',)

class CategoriaServicioViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = CategoriaServicioSerializer
    queryset = CategoriaServicio.objects.filter(estado_obj='A')
    pagination_class = DefaultPagination
    permission_classes = (DefaultPermissions,)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    search_fields = ('id', 'nombre',)

class ProveedorViewSet(viewsets.ModelViewSet):
    serializer_class = ProveedorSerializer
    queryset = Proveedor.objects.filter(estado_obj='A')
    pagination_class = DefaultPagination
    permission_classes = (DefaultPermissions,)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    search_fields = ('id', 'nombre',)

class LocalidadViewSet(viewsets.ModelViewSet):
    serializer_class = LocalidadSerializer
    queryset = Localidad.objects.select_related('ciudad','ciudad__pais').filter(estado_obj='A')
    pagination_class = DefaultPagination
    permission_classes = (DefaultPermissions,)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    search_fields = ('id', 'nombre', 'ciudad__id', 'ciudad__nombre')

class MarcaComercialViewSet(viewsets.ModelViewSet):
    serializer_class = MarcaComercialSerializer
    queryset = MarcaComercial.objects.select_related('proveedor','categoria_servicio','localidad','modalidad_pago').filter(estado_obj='A')
    pagination_class = DefaultPagination
    permission_classes = (DefaultPermissions,)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    search_fields = ('id', 'nombre', 'proveedor__id', 'proveedor__razon_social','categoria_servicio__id','categoria_servicio__nombre','localidad__nombre', 'modalidad_pago__id','modalidad_pago__nombre','direccion','observaciones',)

class TipoCuentaBancoViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = TipoCuentaBancoSerializer
    queryset = TipoCuentaBanco.objects.filter(estado_obj='A')
    pagination_class = DefaultPagination
    permission_classes = (DefaultPermissions,)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    search_fields = ('id', 'nombre',)

class MarcaComercialCuentaViewSet(viewsets.ModelViewSet):
    serializer_class = MarcaComercialCuentaSerializer
    queryset = MarcaComercialCuenta.objects.select_related('marca_comercial','banco','moneda','tipo_cuenta').filter(estado_obj='A')
    pagination_class = DefaultPagination
    permission_classes = (DefaultPermissions,)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend,)
    search_fields = ('id', 'titular',)
    filter_fields = ('marca_comercial',)