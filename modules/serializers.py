from collections import OrderedDict

from rest_framework import serializers
from .models import FotoForBanner, Banner1, Banner2, Banner3, Banner4, Banner5, ModuleForMainPage
#
#
class FotoForBannerSerializer(serializers.ModelSerializer):
    """Сериализер фото для слайдера баннера"""
    # item_number = serializers.IntegerField()
    class Meta:
        model = FotoForBanner
        exclude = ('id',)


class Banner1Serializer(serializers.ModelSerializer):
    """Сериализер баннера № 1"""
    slider = FotoForBannerSerializer(many=True)
    timer = serializers.DateTimeField("%d-%m-%Y - %H:%M:%S")
    class Meta:
        model = Banner1
        fields = ('calendar_title', 'calendar_date', 'text_1', 'slider', 'text_2',
                  'timer_title', 'timer', 'banner_position')


class Banner2Serializer(serializers.ModelSerializer):
    """Сериализер баннера № 2"""
    slider_1 = FotoForBannerSerializer(many=True)
    slider_2 = FotoForBannerSerializer(many=True)
    timer = serializers.DateTimeField("%d-%m-%Y - %H:%M:%S")
    class Meta:
        model = Banner2
        fields = ('calendar_title', 'calendar_date', 'text_1', 'slider_1', 'text_2',
                  'slider_2', 'text_3', 'timer_title', 'timer', 'banner_position')
        depth = 1


class Banner3Serializer(serializers.ModelSerializer):
    """Сериализер баннера № 3"""
    slider = FotoForBannerSerializer(many=True)
    timer = serializers.DateTimeField("%d-%m-%Y - %H:%M:%S")
    class Meta:
        model = Banner3
        fields = ('calendar_title', 'calendar_date', 'text_1', 'slider', 'text_2',
                  'timer_title', 'timer', 'banner_position')


class Banner4Serializer(serializers.ModelSerializer):
    """Сериализер баннера № 4"""
    slider = FotoForBannerSerializer(many=True)
    class Meta:
        model = Banner4
        fields = ('banner_title', 'text_1', 'slider', 'text_2',
                  'banner_position')
        depth = 1


class Banner5Serializer(serializers.ModelSerializer):
    """Сериализер баннера № 5"""
    slider = FotoForBannerSerializer(many=True)
    class Meta:
        model = Banner5
        fields = ('banner_title', 'text_1', 'slider', 'text_2',
                  'banner_position')


class ModuleForMainPageSerializer(serializers.ModelSerializer):

    """Сериализер модуля для главной страницы"""
    banner_type_1 = Banner1Serializer()
    banner_type_2 = Banner2Serializer()
    banner_type_3 = Banner3Serializer()
    banner_type_4 = Banner4Serializer()
    banner_type_5 = Banner5Serializer()

    class Meta:
        model = ModuleForMainPage
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        numbers = []
        banners = []
        result = OrderedDict()
        for value in representation:
            if value.startswith('number_slot_bunner'):
                numbers.append(representation.get(value))
            if value.startswith('banner_type'):
                banners.append(value)
        for_order = list(zip(numbers, banners))
        for value in for_order:
            if value[0] == None or value[1] == None:
                for_order.remove(value)
        order_list = sorted(for_order, key=lambda x: (x[0], x[1]))
        for value in order_list:
            result[value[1]] = representation.get(value[1])
        return result