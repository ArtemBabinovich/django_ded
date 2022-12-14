from rest_framework import viewsets
from main.models import TimeSlideBase
from main.serializers import TimeSlideBaseSerializer


class TimeSlideBaseViewSet(viewsets.ReadOnlyModelViewSet):
    """API Таймер для главного-фотослайдера"""
    queryset = TimeSlideBase.objects.all()
    serializer_class = TimeSlideBaseSerializer


# class TimeForMiniSliderViewSet(viewsets.ReadOnlyModelViewSet):
#     """API Таймер для мини-фотослайдеров"""
#     queryset = TimeForMiniSlider.objects.all()
#     serializer_class = TimeForMiniSliderSerializer
