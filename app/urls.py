from django.conf.urls import url
from app.views import *


urlpatterns = [
    url(r'^$', app_main.as_view(), name='app_main'),
    url(r'^pais/$', app_mantenimiento_pais.as_view(), name='app_mantenimiento_pais'),
    #url(r'^proveedor/$', app_mantenimiento_proveedores.as_view(), name='app_mantenimiento_proveedores'),

    #url(r'^error404/$', error404.as_view()),
    #url(r'^error500/$', error500.as_view()),
]