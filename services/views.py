from rest_framework import viewsets

from services.models import Service, ServiceCatalog
from services.serializers import ServiceSerializer, ServiceCatalogSerializer


class ServiceCatalogViewSet(viewsets.ReadOnlyModelViewSet):
    '''Вывод всех категорий'''
    queryset = ServiceCatalog.objects.all().order_by()
    serializer_class = ServiceCatalogSerializer


class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    """Вывод всех услуг"""
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
