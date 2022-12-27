# from rest_framework import viewsets, mixins
#
# from .models import FotoForBanner, Calendar, Timer, Banner, Module
# from .serializers import FotoForBannerSerializer, CalendarSerializer, TimerSerializer,\
#     BannerSerializer, ModuleSerializer
#
#
# class FotoForBannerViewSet(mixins.ListModelMixin,
#                                 mixins.RetrieveModelMixin,
#                                 viewsets.GenericViewSet):
#     """API фото и текста для слайдера баннера"""
#     queryset = FotoForBanner.objects.all()
#     serializer_class = FotoForBannerSerializer
#
#
# class CalendarViewSet(mixins.ListModelMixin,
#                            mixins.RetrieveModelMixin,
#                            viewsets.GenericViewSet):
#     """API каллендаря"""
#     queryset = Calendar.objects.all()
#     serializer_class = CalendarSerializer
#
#
# class TimerViewSet(mixins.ListModelMixin,
#                            mixins.RetrieveModelMixin,
#                            viewsets.GenericViewSet):
#     """API таймера"""
#     queryset = Timer.objects.all()
#     serializer_class = TimerSerializer
#
#
# class BannerViewSet(mixins.ListModelMixin,
#                            mixins.RetrieveModelMixin,
#                            viewsets.GenericViewSet):
#     """API баннера"""
#     queryset = Banner.objects.all()
#     serializer_class = BannerSerializer
#
#
# class ModuleViewSet(mixins.ListModelMixin,
#                            mixins.RetrieveModelMixin,
#                            viewsets.GenericViewSet):
#     """API модуля"""
#     queryset = Module.objects.all()
#     serializer_class = ModuleSerializer
# # Create your views here.
