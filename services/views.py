from rest_framework import viewsets

from services.models import Service, ServiceCatalog, PromotionsDiscounts
from services.serializers import ServiceSerializer, ServiceCatalogSerializer, PromotionsDiscountsSerializer


class ServiceCatalogViewSet(viewsets.ReadOnlyModelViewSet):
    '''Вывод всех категорий'''
    queryset = ServiceCatalog.objects.all().order_by()
    serializer_class = ServiceCatalogSerializer


class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    """Вывод всех услуг"""
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class PromotionsDiscountsViewSet(viewsets.ReadOnlyModelViewSet):
    """Вывод всех скидок"""
    queryset = PromotionsDiscounts.objects.all()
    serializer_class = PromotionsDiscountsSerializer