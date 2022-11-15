from rest_framework import viewsets
from main.models import FotoSliderBase, TimeSlideBase, TimeForMiniSlider
from main.serializers import FotoSliderBaseSerializer, TimeSlideBaseSerializer, TimeForMiniSliderSerializer


class FotoSliderBaseViewSet(viewsets.ReadOnlyModelViewSet):
    """API Фотослайдер главный"""
    queryset = FotoSliderBase.objects.all()
    serializer_class = FotoSliderBaseSerializer


class TimeSlideBaseViewSet(viewsets.ReadOnlyModelViewSet):
    """API Таймер для главного-фотослайдера"""
    queryset = TimeSlideBase.objects.all()
    serializer_class = TimeSlideBaseSerializer


class TimeForMiniSliderViewSet(viewsets.ReadOnlyModelViewSet):
    """API Таймер для мини-фотослайдеров"""
    queryset = TimeForMiniSlider.objects.all()
    serializer_class = TimeForMiniSliderSerializer
