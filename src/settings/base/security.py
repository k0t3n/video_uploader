from src.settings import env

SECRET_KEY = env.str('SECRET_KEY')

HOSTNAME = env.str('HOSTNAME', default='127.0.0.1')

ALLOWED_HOSTS = [
    HOSTNAME,
    env.str('POD_IP'),
]
