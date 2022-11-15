from rest_framework import serializers

from main.models import FotoSliderBase, TimeSlideBase


class FotoSliderBaseSerializer(serializers.ModelSerializer):
    """Главный фотослайдер"""
    class Meta:
        model = FotoSliderBase
        fields = ['id', 'image', 'text', 'color', 'text_2', 'color_2']


class TimeSlideBaseSerializer(serializers.ModelSerializer):
    """Таймер для главного фотослайдера"""
    class Meta:
        model = TimeSlideBase
        fields = ['id', 'time_pause', ]
