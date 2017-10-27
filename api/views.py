from rest_framework import viewsets
from rest_framework import mixins
from mantenimiento.models import Proveedor
from api.serializers import ProveedorSerializer


class SlinkViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ProveedorSerializer
    queryset = Proveedor.objects.all()