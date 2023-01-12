from django.contrib import admin

from read_tips.models import ContentTips, GeneralModel, ModelTips, PromotionsDiscounts


@admin.register(PromotionsDiscounts)
class PromotionsDiscountsAdmin(admin.ModelAdmin):
    """Модель Акции для читать СОВЕТЫ"""
    list_display = ['title', 'is_activ', 'text']
    list_editable = ['is_activ', ]


@admin.register(GeneralModel)
class GeneralModelAdmin(admin.ModelAdmin):
    """Сборка СОВЕТОВ в один блок"""
    list_display = ['title', 'services_catalog', ]
    list_editable = ['services_catalog', ]
    filter_horizontal = ('advices',)


@admin.register(ModelTips)
class ModelTipsAdmin(admin.ModelAdmin):
    """Создание СОВЕТОВ"""
    list_display = ['title', 'title2', ]
    filter_horizontal = ('content',)


@admin.register(ContentTips)
class ContentTipsAdmin(admin.ModelAdmin):
    """Создание содержания СОВЕТОВ"""
    list_display = ['title', 'description', 'service', 'photo', 'services_catalog']
