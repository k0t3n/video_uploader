from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from apps.videos.views import VideoView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', VideoView.as_view(), name='video')
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns.append(
        path('__debug__/', include(debug_toolbar.urls)),
    )
