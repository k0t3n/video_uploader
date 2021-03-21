INSTALLED_APPS = [
    # Django core
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3d-party apps
    'debug_toolbar',
    'django_celery_beat',

    # project apps
    'apps.users',
    'apps.videos',
]
