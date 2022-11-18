from rest_framework import serializers

from main.models import TimeSlideBase, TimeForMiniSlider


class TimeSlideBaseSerializer(serializers.ModelSerializer):
    """Таймер для главного фотослайдера"""
    class Meta:
        model = TimeSlideBase
        fields = ['id', 'time_pause', ]


class TimeForMiniSliderSerializer(serializers.ModelSerializer):
    """Таймер для мини-фотослайдеров"""
    class Meta:
        model = TimeForMiniSlider
        fields = ['id', 'time_pause', ]
