from rest_framework import serializers
from .models import SocialNetworks, Phone


class SocialNetworksSerializer(serializers.ModelSerializer):
    """Социальная сеть"""
    class Meta:
        model = SocialNetworks
        fields = ['id', 'logo', 'name', 'link',]


class PhoneSerializer(serializers.ModelSerializer):
    """Телефонные номер"""
    class Meta:
        model = Phone
        fields = '__all__'