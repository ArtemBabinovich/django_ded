from rest_framework import serializers

from services.models import ImageForServices, Service, ServiceCatalog


class ServiceCatalogSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceCatalog
        fields = ['title', 'image', 'add_descriptions']


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['title',
                  'image',
                  'image_title',
                  'short_descriptions',
                  'price',
                  'marker',
                  'sort_service']