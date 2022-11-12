from rest_framework import viewsets
from rest_framework.response import Response

from services.models import ServicesCatalog
from services.serializers import ServicesCatalogSerializer


class ServicesCatalogViewSet(viewsets.ReadOnlyModelViewSet):
    """Отоброжение отфильтрованных данных по полю 'Активная'"""
    queryset = ServicesCatalog.objects.filter(is_active=True).filter(services__is_active=True)
    serializer_class = ServicesCatalogSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response({'data': serializer.data})
