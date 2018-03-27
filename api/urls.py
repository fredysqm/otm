from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from api.views import PaisViewSet, CiudadViewSet, IdiomaViewSet, MonedaViewSet


router = DefaultRouter()
router.register(r'pais', PaisViewSet)
router.register(r'ciudad', CiudadViewSet)
router.register(r'idioma', IdiomaViewSet)
router.register(r'moneda', MonedaViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]