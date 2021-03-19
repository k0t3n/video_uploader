from settings import env

CELERY_BROKER_URL = env.url('CELERY_BROKER_URL', default='amqp://localhost')
