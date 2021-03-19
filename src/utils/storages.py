import uuid

from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


# noinspection PyAbstractClass
class VideoThumbnailsStorage(S3Boto3Storage):
    location = f'{settings.MEDIA_DIR}/{settings.THUMBNAILS_DIR}'


# noinspection PyAbstractClass
class UploadedVideosStorage(S3Boto3Storage):
    location = f'{settings.MEDIA_DIR}/{settings.UPLOADED_VIDEOS_DIR}'


# noinspection PyAbstractClass
class EncodedVideosStorage(S3Boto3Storage):
    location = f'{settings.MEDIA_DIR}/{settings.ENCODED_VIDEOS_DIR}'


# noinspection PyAbstractClass
class MediaStorage(S3Boto3Storage):
    location = settings.MEDIA_DIR


def get_file_upload_path(instance, filename):
    return f"{uuid.uuid4()}.{filename.split('.')[-1]}"
