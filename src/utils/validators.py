from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class FileSizeValidator:
    """
    Django validator limiting the maximum file size
    """

    def __init__(self, max_size):
        """
        :param max_size: max file size in bytes
        """
        self.max_size = max_size

    def __call__(self, value):
        if value.file.size > self.max_size:
            raise ValidationError(
                'File size is limited to {} bytes, uploaded file size is {} bytes'.format(
                    self.max_size, value.file.size
                ),
                params={'value': value}
            )
