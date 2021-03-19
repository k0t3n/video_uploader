import os

from settings import env

DEFAULT_FILE_STORAGE = 'src.utils.storages.MediaStorage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'

STATIC_URL = '/static/'
STATIC_ROOT = os.environ.get('STATIC_ROOT', os.path.join(BASE_DIR, 'static'))
UPLOADED_FILE_MAX_SIZE_BYTES = env.int('UPLOADED_FILE_MAX_SIZE_BYTES', 10485760)  # 10mb by default

MEDIA_DIR = 'media'
UPLOADED_VIDEOS_DIR = 'uploaded_videos'
ENCODED_VIDEOS_DIR = 'encoded_videos'
THUMBNAILS_DIR = 'thumbnails'
DEFAULT_THUMBNAIL_URL = 'https://i.kym-cdn.com/entries/icons/original/000/032/100/cover4.jpg'
