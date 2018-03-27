from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from api.views import PaisViewSet, CiudadViewSet


router = DefaultRouter()
router.register(r'pais', PaisViewSet)
router.register(r'ciudad', CiudadViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]