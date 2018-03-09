from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    url(r'^', include('app.urls')),
    url(r'^api/v1/', include('api.urls')),
    url(r'^auth/', include('xauth.urls')),
    url(r'^adminplus/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns