from django.db.models import Prefetch
from django.db.models import Q
from rest_framework import viewsets
from rest_framework.response import Response

from services.models import ServicesCatalog, Services
from services.serializers import ServicesCatalogSerializer, BigSliderSerializer, ServicesCatalogSerializerForSmallSlider


class ServicesCatalogViewSet(viewsets.ReadOnlyModelViewSet):
    """Представление отфильтрованных данных по полю 'Активная'"""
    queryset = ServicesCatalog.objects.filter(is_active=True) \
        .prefetch_related(Prefetch('services', queryset=Services.objects.filter(is_active=True)))
    serializer_class = ServicesCatalogSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response({'data': serializer.data})


class BigSliderViewSet(viewsets.ReadOnlyModelViewSet):
    """Представление большого слайдера"""
    queryset = ServicesCatalog.objects \
        .filter(is_active=True) \
        .prefetch_related(Prefetch('services', queryset=Services.objects.filter(is_active=True)))
    serializer_class = BigSliderSerializer


class SmallSliderViewSet(viewsets.ReadOnlyModelViewSet):
    """Представление маленького слайдера"""

    # TODO: делается в 2 запроса, оптимизировать в один запрос, develop_han
    def get_queryset(self):
        queryset = ServicesCatalog.objects.filter(is_active=True) \
            .prefetch_related(Prefetch('services', queryset=Services.objects
                                       .filter(Q(is_active=True) & ~Q(image_for_mini_slider__exact=''))))
        exclude_items = []
        for item in queryset:
            if item.services.count() == 0:
                exclude_items.append(item.id)
        return queryset.exclude(id__in=exclude_items)

    serializer_class = ServicesCatalogSerializerForSmallSlider
