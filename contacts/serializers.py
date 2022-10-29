from rest_framework import serializers
from .models import SocialNetworks


class SocialNetworksSerializer(serializers.ModelSerializer):
    """Социальная сеть"""
    class Meta:
        model = SocialNetworks
        fields = ['id', 'logo', 'name', 'link',]