from rest_framework import viewsets, mixins

from .models import FotoForBanner, Calendar, Timer, Banner
from .serializers import FotoForBannerSerializer, CalendarSerializer, TimerSerializer,\
    BannerSerializer


class FotoForBannerViewSet(mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                viewsets.GenericViewSet):
    """API фото и текста для слайдера баннера"""
    queryset = FotoForBanner.objects.all()
    serializer_class = FotoForBannerSerializer

class CalendarViewSet(mixins.ListModelMixin,
                           mixins.RetrieveModelMixin,
                           viewsets.GenericViewSet):
    """API каллендаря"""
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer


class TimerViewSet(mixins.ListModelMixin,
                           mixins.RetrieveModelMixin,
                           viewsets.GenericViewSet):
    """API каллендаря"""
    queryset = Timer.objects.all()
    serializer_class = TimerSerializer


class BannerViewSet(mixins.ListModelMixin,
                           mixins.RetrieveModelMixin,
                           viewsets.GenericViewSet):
    """API каллендаря"""
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
# Create your views here.
