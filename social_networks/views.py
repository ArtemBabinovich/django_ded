from django.shortcuts import render
from rest_framework import mixins, viewsets

from social_networks.models import SubscribeSocialNetworksModel
from social_networks.serializers import SubscribeSocialNetworksModelSerializer


class SubscribeSocialNetworksApiView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = SubscribeSocialNetworksModel.objects.all()
    serializer_class = SubscribeSocialNetworksModelSerializer
