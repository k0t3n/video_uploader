from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.db import models
from django.db.models import CheckConstraint, Q
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from apps.videos.choices import EncodedVideoContainerChoices, VideoStatusChoices
from utils.models import TimeStampedModel
from utils.storages import EncodedVideosStorage, get_file_upload_path, UploadedVideosStorage, VideoThumbnailsStorage
from utils.validators import FileSizeValidator


class Video(TimeStampedModel):
    file = models.FileField(
        upload_to=get_file_upload_path,
        validators=[
            FileExtensionValidator(allowed_extensions=settings.AWS_MEDIACONVERT_SUPPORTED_FORMATS),
            FileSizeValidator(max_size=settings.UPLOADED_FILE_MAX_SIZE_BYTES),
        ],
        storage=UploadedVideosStorage,
        blank=True,
        null=True,
    )

    remote_id = models.CharField(
        max_length=64,
        unique=True,
        null=True,
        blank=True,
    )

    status = models.CharField(
        max_length=9,
        choices=VideoStatusChoices.choices,
        default=VideoStatusChoices.CREATED,
    )

    link = models.URLField(
        blank=True,
        null=True,
    )

    thumbnail = models.ImageField(
        blank=True,
        null=True,
        storage=VideoThumbnailsStorage,
    )

    class Meta:
        verbose_name = _('video')
        verbose_name_plural = _('videos')
        constraints = (
            CheckConstraint(
                check=Q(link__isnull=False) | Q(file__isnull=False),
                name='file_or_link_provided'
            ),
        )

    def __str__(self):
        return self.file.name

    @property
    def file_name(self):
        return self.file.name or self.link.split('/')[-1]

    @property
    def url(self):
        return self.link or self.file.url

    @property
    def thumbnail_url(self):
        if self.thumbnail:
            return self.thumbnail.url

        return settings.DEFAULT_THUMBNAIL_URL

    def set_as_failed(self, *args, **kwargs):
        self.status = VideoStatusChoices.FAILED
        self.save(*args, **kwargs)

    def set_as_encoding(self, remote_id, *args, **kwargs):
        self.remote_id = remote_id
        self.status = VideoStatusChoices.ENCODING
        self.save(*args, **kwargs)

    def set_as_succeeded(self, *args, **kwargs):
        self.status = VideoStatusChoices.SUCCEEDED
        self.save(*args, **kwargs)


class EncodedVideo(TimeStampedModel):
    container = models.CharField(
        choices=EncodedVideoContainerChoices.choices,
        max_length=4,
    )

    source = models.ForeignKey(
        to=Video,
        on_delete=models.CASCADE,
        related_name='encoded_videos',
    )

    file = models.FileField(
        storage=EncodedVideosStorage,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _('encoded video')
        verbose_name_plural = _('encoded videos')
        unique_together = ('source', 'container')

    def __str__(self):
        return self.file.name


@receiver(post_save, sender=Video)
def create_encoding_task(sender, instance, created, *args, **kwargs):
    from apps.videos.tasks import create_encoding_job

    if created:
        create_encoding_job.delay(video_id=instance.id)
