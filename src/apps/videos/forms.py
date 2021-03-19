from django import forms
from django.core.exceptions import ValidationError

from src.apps.videos.models import Video


class VideoUploadForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('file', 'link')

    def clean(self):
        file, link = self.cleaned_data['file'], self.cleaned_data['link']
        if not any((file, link)) or all((file, link)):
            raise ValidationError('File or link must be provided')

        return super(VideoUploadForm, self).clean()
