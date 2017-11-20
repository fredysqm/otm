from django.conf.urls import url
from xauth.views import *


urlpatterns = [
    url(r'^login/$', xauth_login.as_view(), name='xauth_login'),
    url(r'^logout/$', xauth_logut.as_view(), name='xauth_logout'),
    url(r'^password/change/$', xauth_password_change.as_view(), name='xauth_password_change'),
    url(r'^password/change/done/$', xauth_password_change_done.as_view(), name='xauth_password_change_done'),
]