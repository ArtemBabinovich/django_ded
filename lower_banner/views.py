from django.shortcuts import render
from rest_framework import mixins, viewsets
from rest_framework.response import Response

from .models import LowerBannerForMainPage
from .serializers import LowerBannerForMainPageSerializer


class LowerBannerForMainPageViewSet(mixins.RetrieveModelMixin,
                                viewsets.GenericViewSet):
    """API нижнего баннера для главной страницы"""
    queryset = LowerBannerForMainPage.objects.all()
    serializer_class = LowerBannerForMainPageSerializer

    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_queryset().last()
        serializer = LowerBannerForMainPageSerializer(queryset)
        return Response(serializer.data)


# Create your views here.
