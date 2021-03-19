from django.contrib import admin

from .models import EncodedVideo, Video


class EncodedViewInline(admin.TabularInline):
    model = EncodedVideo
    extra = 0


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    inlines = (EncodedViewInline,)
    list_display = ('id', 'remote_id', 'file', 'status',)
    list_filter = ('status',)
