# from rest_framework import serializers
# from .models import FotoForLowerBanner, TextForLowerBanner, LowerBanner1, LowerBanner2,\
#     LowerBanner3, AllLowerBanners, LowerBannerForMainPage
#
#
# class FotoForLowerBannerSerializer(serializers.ModelSerializer):
#     """Сериализер фото для слайдера нижнего баннера"""
#
#     class Meta:
#         model = FotoForLowerBanner
#         exclude = ('id',)
#
#
# class TextForLowerBannerSerializer(serializers.ModelSerializer):
#     """Сериализер ссылок для слайдера нижнего баннера"""
#     class Meta:
#         model = TextForLowerBanner
#         exclude = ('id', 'title')
#
#
# class LowerBanner1Serializer(serializers.ModelSerializer):
#     """Сериализер нижнего баннера №1"""
#     slider = FotoForLowerBannerSerializer(many=True)
#     link_block_1 = TextForLowerBannerSerializer(many=True)
#     link_block_2 = TextForLowerBannerSerializer(many=True)
#     link_block_3 = TextForLowerBannerSerializer(many=True)
#
#     class Meta:
#         model =  LowerBanner1
#         fields = ('slider', 'link_block_1', 'link_block_2', 'link_block_3',
#                   'calendar_date', 'timer',)
#
#
# class LowerBanner2Serializer(serializers.ModelSerializer):
#     """Сериализер нижнего баннера №2"""
#     slider_1 = FotoForLowerBannerSerializer(many=True)
#     link_block_1 = TextForLowerBannerSerializer(many=True)
#     link_block_2 = TextForLowerBannerSerializer(many=True)
#     slider_2 = FotoForLowerBannerSerializer(many=True)
#
#     class Meta:
#         model = LowerBanner2
#         fields = ('slider_1', 'link_block_1', 'link_block_2', 'slider_2',)
#
#
# class LowerBanner3Serializer(serializers.ModelSerializer):
#     """Сериализер нижнего баннера №3"""
#     slider_1 = FotoForLowerBannerSerializer(many=True)
#     link_block_1 = TextForLowerBannerSerializer(many=True)
#     slider_2 = FotoForLowerBannerSerializer(many=True)
#     link_block_2 = TextForLowerBannerSerializer(many=True)
#
#     class Meta:
#         model = LowerBanner3
#         fields = ('slider_1', 'link_block_1', 'slider_2', 'link_block_2',)
#
#
# class AllLowerBannersSerializer(serializers.ModelSerializer):
#     """Сериализер модели всех баннеров"""
#     low_banner_1 = LowerBanner1Serializer()
#     low_banner_2 = LowerBanner2Serializer()
#     low_banner_3 = LowerBanner3Serializer()
#
#     class Meta:
#         model = AllLowerBanners
#         exclude = ('id',)
#
#     def to_representation(self, instance):
#         """Удаление объектов равных null из 'json'-а"""
#         representation = super().to_representation(instance)
#         copy_representation = representation.copy()
#         for i in copy_representation:
#             if copy_representation[i] == None:
#                 representation.pop(i)
#         return representation
#
#
# class LowerBannerForMainPageSerializer(serializers.ModelSerializer):
#     """Сериализатор нижнего баннера главной страницы"""
#     selected_banners = AllLowerBannersSerializer(many=True)
#
#     class Meta:
#         model = LowerBannerForMainPage
#         exclude = ('id',)