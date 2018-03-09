from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from api.views import PaisViewSet


router = DefaultRouter()
router.register(r'pais', PaisViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]