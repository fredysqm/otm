from django.urls import path, include
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    path( '', include('app.urls') ),
    path( 'api/v1/', include('api.urls') ),
    path( 'auth/', include('xauth.urls') ),
    path( 'adminplus/', admin.site.urls ),
]

if settings.DEBUG:
    from django.conf.urls import url
    import debug_toolbar
    urlpatterns = [
        url( r'^__debug__/', include(debug_toolbar.urls) ),
    ] + urlpatterns