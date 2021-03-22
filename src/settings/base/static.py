import os

from settings import env

DEFAULT_FILE_STORAGE = 'utils.storages.MediaStorage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'

STATIC_URL = '/static/'
STATIC_ROOT = os.environ.get('STATIC_ROOT', os.path.join(BASE_DIR, 'static'))
UPLOAD_FILE_MAX_SIZE_BYTES = env.int('UPLOAD_FILE_MAX_SIZE_MB', 10) * 1024 * 1024

MEDIA_DIR = 'media'
UPLOAD_VIDEOS_DIR = 'uploaded_videos'
ENCODE_VIDEOS_DIR = 'encoded_videos'
THUMBNAILS_DIR = 'thumbnails'
DEFAULT_THUMBNAIL_URL = 'https://i.kym-cdn.com/entries/icons/original/000/032/100/cover4.jpg'
