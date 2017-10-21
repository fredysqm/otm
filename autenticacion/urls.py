from django.conf.urls import url
from autenticacion.views import *


urlpatterns = [
    url(r'^login/$', autenticacion_login.as_view(), name='autenticacion_login'),
    url(r'^logout/$', autenticacion_logut.as_view(), name='autenticacion_logout'),
    url(r'^password/change/$', autenticacion_password_change.as_view(), name='autenticacion_password_change'),
    url(r'^password/change/done/$', autenticacion_password_change_done.as_view(), name='autenticacion_password_change_done'),
]