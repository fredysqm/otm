from django.conf.urls import url
from app.views import *


urlpatterns = [
    url(r'^$', app_main.as_view(), name='app_main'),
    url(r'^pais/$', app_mantenimiento_pais.as_view(), name='app_mantenimiento_pais'),
    url(r'^ciudad/$', app_mantenimiento_ciudad.as_view(), name='app_mantenimiento_ciudad'),
    url(r'^idioma/$', app_mantenimiento_idioma.as_view(), name='app_mantenimiento_idioma'),
    url(r'^moneda/$', app_mantenimiento_moneda.as_view(), name='app_mantenimiento_moneda'),
    url(r'^banco/$', app_mantenimiento_banco.as_view(), name='app_mantenimiento_banco'),
    url(r'^operador/$', app_mantenimiento_operador.as_view(), name='app_mantenimiento_operador'),
    url(r'^proveedor/$', app_mantenimiento_proveedor.as_view(), name='app_mantenimiento_proveedor'),

    #url(r'^error404/$', error404.as_view()),
    #url(r'^error500/$', error500.as_view()),
]