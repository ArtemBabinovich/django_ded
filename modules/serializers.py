from rest_framework import serializers
from .models import FotoForBanner, Calendar, Timer, Banner, Module


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
                  'slider_speed', 'timer', 'url', 'text']


class ModuleSerializer(serializers.ModelSerializer):
    """Сериализер для модуля"""
    slot_1 = BannerSerializer()
    slot_2 = BannerSerializer()
    slot_3 = BannerSerializer()
    slot_4 = BannerSerializer()
    slot_5 = BannerSerializer()
    class Meta:
        model = Module
        fields = ['id', 'name', 'slot_1', 'slot_2', 'slot_3', 'slot_4', 'slot_5',]