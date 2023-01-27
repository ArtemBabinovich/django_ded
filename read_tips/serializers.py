from rest_framework import serializers

from read_tips.models import ContentTips, ModelTips, GeneralModel, PromotionsDiscounts
from services.models import ServicesCatalog, Services


class ServicesSerializer1(serializers.ModelSerializer):
    """Сериализатор для УСЛУГ"""

    class Meta:
        model = Services
        fields = ['service_title', 'url']


class ServicesCategorySerializer(serializers.ModelSerializer):
    """Сериализатор для КАКЛОГА-УСЛУГ"""

    class Meta:
        model = ServicesCatalog
        fields = ['title', 'url', ]


class PromotionsDiscountsSerializer(serializers.ModelSerializer):
    """Сериализатор для СКИДОК """

    class Meta:
        model = PromotionsDiscounts
        fields = ['text']


class ContentTipsSerializer(serializers.ModelSerializer):
    """Сериализатор для СОДЕРЖИМОГО СОВЕТОВ"""
    service = ServicesSerializer1()
    services_catalog = ServicesCategorySerializer()

    class Meta:
        model = ContentTips
        fields = ['title', 'url', 'description', 'service', 'photo', 'services_catalog']


class ModTipServSer(serializers.ModelSerializer):
    """Сериализатор для СОВЕТОВ"""
    content = ContentTipsSerializer(many=True)

    class Meta:
        model = ModelTips
        fields = ['title', 'title2', 'content', ]


class ContentTipsServSer1(serializers.ModelSerializer):
    """Сериализатор для сборки якорей"""

    class Meta:
        model = ContentTips
        fields = ['title', 'url']


class GeneralModelSerializer(serializers.ModelSerializer):
    """Сериализатор для сборки общего блока читать СОВЕТЫ"""
    advices_url = serializers.SerializerMethodField()
    advices = ModTipServSer(many=True)
    discount = PromotionsDiscountsSerializer()

    class Meta:
        model = GeneralModel
        fields = ['discount', 'advices_url', 'advices', ]

    # функция фильтрует все урлы и названия в собраном блоке
    def get_advices_url(self, obj):
        queryset = ContentTips.objects.filter(modeltips__general__title=obj)
        serializer = ContentTipsServSer1(queryset, many=True)
        return serializer.data

# class MainSerializer(serializers.ModelSerializer):
#     """Главный сериализатор для общего API"""
#     advices_for_services_catalog = GeneralModelSerializer(many=True)
#
#     class Meta:
#         model = ServicesCatalog
#         fields = ['advices_for_services_catalog']
