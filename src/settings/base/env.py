from src.settings import env

DEBUG = env.bool('DEBUG', default=False)

ENVIRONMENT_PRODUCTION = 'production'
ENVIRONMENT_STAGING = 'staging'
ENVIRONMENT_LOCAL = 'local'
ENVIRONMENT_CI = 'ci'
ENVIRONMENT = env.str('ENVIRONMENT', default=ENVIRONMENT_PRODUCTION)
