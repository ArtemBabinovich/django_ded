from django.contrib import admin

from video_app.models import Video


@admin.register(Video)
class VideoModel(admin.ModelAdmin):
    """Модель для добавления ссылок для видео"""
    fields = ('title', 'url', 'description', 'is_active', 'description2')
    list_display = ('title', 'url', 'is_active',)
    list_editable = ['is_active']
