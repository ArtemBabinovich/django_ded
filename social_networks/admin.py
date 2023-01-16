from django.contrib import admin
from django.utils.safestring import mark_safe

from social_networks.models import AddSocialNetworks, SubscribeSocialNetworksModel


@admin.register(SubscribeSocialNetworksModel)
class SubscribeSocialNetworksModelAdmin(admin.ModelAdmin):
    """Сооздание блока ссылок на социальные сети"""
    fields = ['title', 'title2', 'social_networks', ]
    list_display = ['title', 'title2', ]
    filter_horizontal = ('social_networks',)

@admin.register(AddSocialNetworks)
class AddSocialNetworksAdmin(admin.ModelAdmin):
    """Создание ссылок на социальные сети"""
    fields = ['name', 'url_social_network', ('icon_for_url', 'get_icon_for_url',), 'image', ]
    readonly_fields = ('get_icon_for_url',)
    list_display = ['name', 'url_social_network', 'get_icon_for_url',]

    # функци для отображения изображения в админке
    def get_icon_for_url(self, obj):
        return mark_safe(f'<img src={obj.icon_for_url.url} width="50" height="50">')

    get_icon_for_url.short_description = 'Иконка соц.сети'