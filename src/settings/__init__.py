from pathlib import Path

import environ
from split_settings.tools import include, optional

env = environ.Env()
environ.Env.read_env(env_file=str(Path(__file__).parents[2]) + '/.env')

include(
    'base/env.py', optional('local/env.py'),
    'base/root.py',
    'base/common.py',
    'base/logging.py', optional('local/logging.py'),
    'base/security.py', optional('local/security.py'),
    'base/middleware.py',
    'base/apps.py',
    'base/static.py',
    'base/*.py',

    optional('local/*.py'),
)
