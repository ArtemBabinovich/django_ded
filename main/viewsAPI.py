from rest_framework import viewsets
from main.models import FotoSliderBase, TimeSlideBase, MiniFotoSlider, TimeForMiniSlider
from main.serializers import FotoSliderBaseSerializer, TimeSlideBaseSerializer, MiniFotoSliderSerializer, \
    TimeForMiniSliderSerializer


class FotoSliderBaseViewSet(viewsets.ReadOnlyModelViewSet):
    """API Фотослайдер главный"""
    queryset = FotoSliderBase.objects.all()
    serializer_class = FotoSliderBaseSerializer


class TimeSlideBaseViewSet(viewsets.ReadOnlyModelViewSet):
    """API Фотослайдер главный"""
    queryset = TimeSlideBase.objects.all()
    serializer_class = TimeSlideBaseSerializer


class MiniFotoSliderViewSet(viewsets.ReadOnlyModelViewSet):
    """API Мини-слайдер"""
    queryset = MiniFotoSlider.objects.all()
    serializer_class = MiniFotoSliderSerializer


class TimeForMiniSliderViewSet(viewsets.ReadOnlyModelViewSet):
    """API таймер Мини-слайдер"""
    queryset = TimeForMiniSlider.objects.all()
    serializer_class = TimeForMiniSliderSerializer
