from rest_framework import viewsets
from main.models import FotoSliderBase, TimeSlideBase
from main.serializers import FotoSliderBaseSerializer, TimeSlideBaseSerializer



class FotoSliderBaseViewSet(viewsets.ReadOnlyModelViewSet):
    """API Фотослайдер главный"""
    queryset = FotoSliderBase.objects.all()
    serializer_class = FotoSliderBaseSerializer


class TimeSlideBaseViewSet(viewsets.ReadOnlyModelViewSet):
    """API Фотослайдер главный"""
    queryset = TimeSlideBase.objects.all()
    serializer_class = TimeSlideBaseSerializer
