import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

ROOT_URLCONF = 'otm.urls'
WSGI_APPLICATION = 'otm.wsgi.application'

LANGUAGE_CODE = 'es-PE'
USE_I18N = True
USE_L10N = False
TIME_ZONE = 'America/Lima'
DATETIME_FORMAT = 'd/m/Y H:i'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates"),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFilesStorage'

COMPRESS_CSS_FILTERS = (
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
)

COMPRESS_OUTPUT_DIR = ''

CRISPY_TEMPLATE_PACK = 'bootstrap3'

LOGIN_URL = '/auth/login'
LOGIN_REDIRECT_URL = '/'
#LOGOUT_REDIRECT_URL = '/'

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'localhost:11211',
    }
}