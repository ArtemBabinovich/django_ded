from django.contrib import admin

from video_app.models import Video


@admin.register(Video)
class VideoModel(admin.ModelAdmin):
    """Модель для добавления ссылок для видео"""
    fields = ('url', 'description', 'is_active', 'description2')
    list_display = ('url', 'is_active', 'description',)
    list_editable = ['is_active']
