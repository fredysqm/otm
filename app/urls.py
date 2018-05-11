from django.urls import path
from app.views import *


urlpatterns = [
    path('', app_main.as_view(), name='app_main'),
    path('proveedores/', app_proveedor.as_view(), name='app_proveedor'),

    #url(r'^error404/$', error404.as_view()),
    #url(r'^error500/$', error500.as_view()),
]