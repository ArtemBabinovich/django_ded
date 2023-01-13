from django.contrib import admin

from social_networks.models import AddSocialNetworks, SubscribeSocialNetworksModel


@admin.register(SubscribeSocialNetworksModel)
class SubscribeSocialNetworksModelAdmin(admin.ModelAdmin):
    fields = ['title', 'title2', 'social_networks', ]
    list_display = ['title', 'title2', ]
    filter_horizontal = ('social_networks',)

@admin.register(AddSocialNetworks)
class AddSocialNetworksAdmin(admin.ModelAdmin):
    fields = ['url_social_network', 'icon_for_url', 'image', ]
    list_display = ['icon_for_url', 'url_social_network', ]