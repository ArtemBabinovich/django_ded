from rest_framework import viewsets, mixins
from rest_framework.response import Response
import json
from .models import ModuleForMainPage
from .serializers import ModuleForMainPageSerializer
#
#
class ModuleForMainPageViewSet(mixins.RetrieveModelMixin,
                                viewsets.GenericViewSet):
    """API модуля для главной страницы"""
    queryset = ModuleForMainPage.objects.all()
    serializer_class = ModuleForMainPageSerializer

    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_queryset().last()
        serializer = ModuleForMainPageSerializer(queryset)
        # response = serializer.order(serializer.data)
        return Response(serializer.data)