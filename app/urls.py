from django.conf.urls import url
from app.views import *


urlpatterns = [
    url(r'^$', app_main.as_view(), name='app_main'),
    url(r'^proveedores/$', app_proveedor.as_view(), name='app_proveedor'),

    #url(r'^error404/$', error404.as_view()),
    #url(r'^error500/$', error500.as_view()),
]