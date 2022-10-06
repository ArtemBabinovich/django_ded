from rest_framework import serializers

from main.models import FotoSliderBase, TimeSlideBase


class FotoSliderBaseSerializer(serializers.ModelSerializer):
    """Главный фотослайдер"""
    class Meta:
        model = FotoSliderBase
        fields = ['image', 'text']


class TimeSlideBaseSerializer(serializers.ModelSerializer):
    """Таймер для главного фотослайдера"""
    class Meta:
        model = TimeSlideBase
        fields = ['time_pause', ]
