from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from api.views import PaisViewSet, CiudadViewSet, IdiomaViewSet, MonedaViewSet, BancoViewSet, OperadorViewSet


router = DefaultRouter()
router.register(r'pais', PaisViewSet)
router.register(r'ciudad', CiudadViewSet)
router.register(r'idioma', IdiomaViewSet)
router.register(r'moneda', MonedaViewSet)
router.register(r'banco', BancoViewSet)
router.register(r'operador', OperadorViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]