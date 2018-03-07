"""
Django local settings for otm project.
"""

DEBUG = True
ALLOWED_HOSTS = []
SECRET_KEY = 'v1y*lebn2rk*%w(h(7ivq(w)ipwngwvw%mc*-trmphouz+g(cb'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'otm',
        'USER': 'root',
        'PASSWORD': 'pwd123',
        'HOST': 'localhost',
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = '/tmp/static/'
