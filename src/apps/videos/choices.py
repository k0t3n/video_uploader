from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class VideoStatusChoices(TextChoices):
    CREATED = 'created'
    ENCODING = 'encoding'
    SUCCEEDED = 'succeeded'
    FAILED = 'failed'


class EncodedVideoContainerChoices(TextChoices):
    WEBM = 'webm', _('webm')
    MP4 = 'mp4', _('mp4')
