from settings import env

DATABASES = {
    'default': {
        **env.db(),
        'CONN_MAX_AGE': 60,
    },
}
