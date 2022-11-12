from rest_framework import viewsets
from .models import SocialNetworks, Phone
from .serializers import SocialNetworksSerializer, PhoneSerializer


class SocialNetworksViewSet(viewsets.ReadOnlyModelViewSet):
    """API Социальной сети"""
    queryset = SocialNetworks.objects.all()
    serializer_class = SocialNetworksSerializer


class PhoneViewSet(viewsets.ReadOnlyModelViewSet):
    """API телефонного номера"""
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer