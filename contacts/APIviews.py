from rest_framework import viewsets
from .models import SocialNetworks
from .serializers import SocialNetworksSerializer


class SocialNetworksViewSet(viewsets.ReadOnlyModelViewSet):
    """API Социальной сети"""
    queryset = SocialNetworks.objects.all()
    serializer_class = SocialNetworksSerializer
