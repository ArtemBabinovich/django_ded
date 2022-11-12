from rest_framework import serializers

from services.models import ServicesCatalog, Services


class ServicesSerializer(serializers.ModelSerializer):
    """Сериализатор для УСЛУГ"""

    class Meta:
        model = Services
        fields = [
            'position_service',
            'service_title',
            'additional_title',
            'marker',
            'image_for_mini_slider',
            'bottom_description'
        ]


class ServicesCatalogSerializer(serializers.ModelSerializer):
    """Сериализатор для РАЗДЕЛА УСЛУГ"""
    services_set = ServicesSerializer(many=True)

    class Meta:
        model = ServicesCatalog
        fields = ['position', 'title', 'additional_title', 'image_for_big_slider', 'url', 'services_set']
