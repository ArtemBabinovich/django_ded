from rest_framework import serializers

from video_app.models import Video


class VideoSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Video"""
    class Meta:
        model = Video
        fields = ['url', 'description', 'is_active', 'description2']
