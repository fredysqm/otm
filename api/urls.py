from django.urls import path, include
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
router.register(r'categoria_servicio', CategoriaServicioViewSet)
router.register(r'proveedor', ProveedorViewSet)
router.register(r'localidad', LocalidadViewSet)
router.register(r'marca_comercial', MarcaComercialViewSet)
router.register(r'tipo_cuenta_banco', TipoCuentaBancoViewSet)
router.register(r'marca_comercial_cuenta', MarcaComercialCuentaViewSet)


urlpatterns = [
    path( '', include(router.urls) ),
]