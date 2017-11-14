from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import pagination
from rest_framework import filters
from mantenimiento.models import Proveedor
from api.serializers import ProveedorSerializer


class DefaultPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class ProveedorViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
    pagination_class = DefaultPagination
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    search_fields = ('@_searchtext',)
    #ordering_fields = ('username', 'email')
