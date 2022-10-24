from rest_framework import serializers

from main.models import FotoSliderBase, TimeSlideBase, MiniFotoSlider, TimeForMiniSlider


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


class MiniFotoSliderSerializer(serializers.ModelSerializer):
    """Мини-фотослайдер"""
    class Meta:
        model = MiniFotoSlider
        fields = ['id', 'image', 'text_1', 'color_1', 'text_2', 'color_2', 'text_3', 'color_3']


class TimeForMiniSliderSerializer(serializers.ModelSerializer):
    """Таймер для мини-фотослайдера"""
    class Meta:
        model = TimeForMiniSlider
        fields = ['id', 'time_pause', ]
