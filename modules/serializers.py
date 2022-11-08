from rest_framework import serializers
from .models import FotoForBanner, Calendar, Timer, Banner


class FotoForBannerSerializer(serializers.ModelSerializer):
    """Сериализер фото для слайдера баннера"""
    class Meta:
        model = FotoForBanner
        fields = '__all__'


class CalendarSerializer(serializers.ModelSerializer):
    """Сериализер для каллендаря"""
    class Meta:
        model = Calendar
        fields = ['banner_calendar', ]


class TimerSerializer(serializers.ModelSerializer):
    """Сериализер для таймера"""
    class Meta:
        model = Timer
        fields = '__all__'


class BannerSerializer(serializers.ModelSerializer):
    """Сериализер для баннера"""
    calendar = CalendarSerializer()
    slider_fotos = FotoForBannerSerializer(many=True)
    timer = TimerSerializer()
    class Meta:
        model = Banner
        fields = ['id', 'name', 'calendar', 'slider_type', 'slider_fotos',
                  'slider_speed', 'foto_count', 'timer', 'url', 'text']