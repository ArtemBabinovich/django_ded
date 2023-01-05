from rest_framework import serializers
from .models import FotoForBanner, Banner1, Title1ForBanner2, Title2ForBanner2, Banner2, Banner3,\
    TextForBanner4, Banner4, Banner5, ModuleForMainPage

class FotoForBannerSerializer(serializers.ModelSerializer):
    """Сериализер фото для слайдера баннера"""
    # item_number = serializers.IntegerField()
    class Meta:
        model = FotoForBanner
        exclude = ('id',)


class Banner1Serializer(serializers.ModelSerializer):
    """Сериализер баннера № 1"""
    slider = FotoForBannerSerializer(many=True)
    class Meta:
        model = Banner1
        exclude = ('id',)


class Banner2Serializer(serializers.ModelSerializer):
    """Сериализер баннера № 2"""
    slider_1 = FotoForBannerSerializer(many=True)
    slider_2 = FotoForBannerSerializer(many=True)
    class Meta:
        model = Banner2
        exclude = ('id',)
        depth = 1


class Banner3Serializer(serializers.ModelSerializer):
    """Сериализер баннера № 3"""
    slider = FotoForBannerSerializer(many=True)
    class Meta:
        model = Banner3
        exclude = ('id',)


class Banner4Serializer(serializers.ModelSerializer):
    """Сериализер баннера № 4"""
    slider = FotoForBannerSerializer(many=True)
    class Meta:
        model = Banner4
        exclude = ('id',)
        depth = 1


class Banner5Serializer(serializers.ModelSerializer):
    """Сериализер баннера № 5"""
    slider = FotoForBannerSerializer(many=True)
    class Meta:
        model = Banner5
        exclude = ('id',)


class ModuleForMainPageSerializer(serializers.ModelSerializer):

    """Сериализер модуля для главной страницы"""
    banner_type_1 = Banner1Serializer()
    banner_type_2 = Banner2Serializer()
    banner_type_3 = Banner3Serializer()
    banner_type_4 = Banner4Serializer()
    banner_type_5 = Banner5Serializer()

    def order(self, data):
        numbers = []
        banners = []
        result = {}
        for number_slot in data:
            if number_slot.startswith('number_slot_bunner'):
                numbers.append(data.get(number_slot))
        for banner in data:
            if banner.startswith('banner_type'):
                banners.append(banner)
        zipped_values = zip(numbers, banners)
        for_order = list(zipped_values)
        for value in for_order:
            if value[0] == None or value[1] == None:
                for_order.remove(value)
        order_list = sorted(for_order, key=lambda x: (x[0], x[1]))
        for value in order_list:
            result[value[1]] = data.get(value[1])
        return result

    class Meta:
        model = ModuleForMainPage
        exclude = ('id',)
