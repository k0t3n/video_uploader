from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from apps.videos.forms import VideoUploadForm
from apps.videos.models import Video


class VideoView(CreateView):
    form_class = VideoUploadForm
    template_name = 'index.html'
    success_url = reverse_lazy('video')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['videos'] = Video.objects.prefetch_related('encoded_videos')
        return context
