from rest_framework import serializers

from services.models import ServicesCatalog, Services


class ServicesSerializer(serializers.ModelSerializer):
    """Сериализатор для УСЛУГ"""

    class Meta:
        model = Services
        fields = [
            'position_service',
            'id',
            'service_title',
            'marker'
        ]


class ServicesCatalogSerializer(serializers.ModelSerializer):
    """Сериализатор для РАЗДЕЛА УСЛУГ"""
    services = ServicesSerializer(many=True)

    class Meta:
        model = ServicesCatalog
        fields = ['position', 'id', 'title', 'color_title', 'additional_title', 'url', 'services']


class BigSliderSerializer(serializers.ModelSerializer):
    """Сериализатор для большого слайдера"""

    class Meta:
        model = ServicesCatalog
        fields = ['position', 'id', 'title', 'additional_title', 'color_title', 'image_for_big_slider', 'url']


class SmallSliderSerializer(serializers.ModelSerializer):
    """Сериализтор для маленького слайдера"""

    class Meta:
        model = Services
        fields = [
            'id',
            'service_title',
            'color_service_title',
            'image_for_mini_slider',
            'bottom_description',
            'color_bottom_description',
        ]


class ServicesCatalogSerializerForSmallSlider(serializers.ModelSerializer):
    """Сериализатор для маленького слайдера"""
    services = SmallSliderSerializer(many=True)

    class Meta:
        model = ServicesCatalog
        fields = [
            'id',
            'title',
            'additional_title',
            'additional_title_2',
            'color_title',
            'time_pause_for_mini_slider',
            'url',
            'services',
        ]
