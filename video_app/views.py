from rest_framework import viewsets, mixins

from video_app.models import Video
from video_app.serializers import VideoSerializer


class VideoApiViewSets(mixins.ListModelMixin, viewsets.GenericViewSet):
    """API для активных ссылок на видео"""
    queryset = Video.objects.filter(is_active=True)
    serializer_class = VideoSerializer
