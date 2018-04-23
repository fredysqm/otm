from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from api.views import *


router = DefaultRouter()
router.register(r'pais', PaisViewSet)
router.register(r'ciudad', CiudadViewSet)
router.register(r'idioma', IdiomaViewSet)
router.register(r'moneda', MonedaViewSet)
router.register(r'banco', BancoViewSet)
router.register(r'operador', OperadorViewSet)
router.register(r'tipo_doc_proveedor', TipoDocProveedorViewSet)
router.register(r'modalidad_pago', ModalidadPagoViewSet)
router.register(r'tipo_servicio', TipoDocProveedorViewSet)
router.register(r'proveedor', ProveedorViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]