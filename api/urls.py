from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
#from api.views import ProveedorViewSet


router = DefaultRouter()
#router.register(r'proveedor', ProveedorViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]