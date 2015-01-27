from os.path import abspath, join, dirname
PROJECT_ROOT = abspath(dirname(__file__))
REPOSITORY_ROOT = abspath(join(PROJECT_ROOT, '..'))
CACHE_ROOT = abspath(join(REPOSITORY_ROOT, '.cache'))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'rohypnol_test'
    }

}
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': CACHE_ROOT,
    }
}
SECRET_KEY = 'xxx'
ROOT_URLCONF = ''
SITE_ID = 1
INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'rohypnol',
)

MIDDLEWARE_CLASSES = ()