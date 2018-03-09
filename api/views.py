from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import pagination
from rest_framework import filters
from rest_framework import permissions
from core.models import Pais
from api.serializers import PaisSerializder


class DefaultPagination(pagination.PageNumberPagination):
    page_size_query_param = 'page_size'
    page_size = 10
    max_page_size = 100

class PaisViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = PaisSerializder
    queryset = Pais.objects.all()
    pagination_class = DefaultPagination
    permission_classes = (permissions.DjangoModelPermissions,)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    search_fields = ('id', 'nombre',)


# class ProveedorViewSet(viewsets.ModelViewSet):
#     queryset = Proveedor.objects.all()
#     serializer_class = ProveedorSerializer
#     pagination_class = DefaultPagination
#     permission_classes = (permissions.DjangoModelPermissions,)
#     filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
#     search_fields = ('@_fts',)