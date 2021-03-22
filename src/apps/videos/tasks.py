import logging

from django.db import transaction

from apps.videos.choices import EncodedVideoContainerChoices, VideoStatusChoices
from apps.videos.models import EncodedVideo, Video
from celery_app import app
from utils.aws import generate_mediaconvert_encode_job_config, get_mediaconvert_client
from utils.storages import EncodedVideosStorage, VideoThumbnailsStorage

logger = logging.getLogger(__name__)


@app.task
def update_encoding_tasks():
    client = get_mediaconvert_client()

    for video_id in Video.objects.filter(status=VideoStatusChoices.ENCODING).values_list('id', flat=True):
        with transaction.atomic():
            video = Video.objects.select_for_update().get(id=video_id, status=VideoStatusChoices.ENCODING)

            try:
                job = client.get_job(Id=video.remote_id)['Job']
            except client.exceptions.ClientError as error:
                logger.error(error, exc_info=True)
                video.set_as_failed()
                continue

            if job['Status'] == 'COMPLETE':
                base_file_name = video.file.name.split('.')[0]
                encoded_videos = []
                for container in EncodedVideoContainerChoices.values:
                    file_name = f'{base_file_name}.{container}'

                    if not EncodedVideosStorage().exists(file_name):
                        logger.error(f'Unable to find {file_name} in videos storage')
                        transaction.set_rollback(True)
                        break

                    encoded_videos.append(EncodedVideo(
                        container=container,
                        source=video,
                        file=file_name
                    ))

                if transaction.get_rollback():
                    continue

                EncodedVideo.objects.bulk_create(encoded_videos)

                # AWS automatically adds number of frame to the file name
                # it is not controlled by nameModifier :(
                # https://docs.aws.amazon.com/mediaconvert/latest/ug/file-group-with-frame-capture-output.html
                thumbnail_name = f'{base_file_name}.0000000.jpg'
                if not VideoThumbnailsStorage().exists(thumbnail_name):
                    logger.error(f'Unable to find {thumbnail_name} in thumbnail storage')
                    transaction.set_rollback(True)
                    continue

                video.thumbnail = thumbnail_name
                video.set_as_succeeded()

            elif job['Status'] in ('SUBMITTED', 'PROGRESSING'):
                continue
            else:
                video.set_as_failed()


@app.task
@transaction.atomic
def create_encoding_job(video_id):
    video = Video.objects.select_for_update().get(id=video_id, status=VideoStatusChoices.CREATED)
    client = get_mediaconvert_client()
    config = generate_mediaconvert_encode_job_config(file_url=video.url)

    try:
        job = client.create_job(**config)['Job']
    except client.exceptions.ClientError as error:
        logger.error(error, exc_info=True)
        video.set_as_failed()
        return

    video.set_as_encoding(remote_id=job['Id'])
