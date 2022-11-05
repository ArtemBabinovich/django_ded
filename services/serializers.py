from rest_framework import serializers

from services.models import ImageForTextDetailService, Service, ServiceCatalog, PromotionsDiscounts


class PromotionsDiscountsSerializer(serializers.ModelSerializer):

    class Meta:
        model = PromotionsDiscounts
        fields = '__all__'

class ServiceCatalogSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceCatalog
        fields = '__all__'
        # fields = ['title', 'image', 'add_descriptions']


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
        # fields = ['title',
        #           'image',
        #           'image_title',
        #           'short_descriptions',
        #           'price',
        #           'marker',
        #           'sort_service']