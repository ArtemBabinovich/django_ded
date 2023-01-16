from rest_framework import serializers

from social_networks.models import SubscribeSocialNetworksModel, AddSocialNetworks


class AddSocialNetworksSerializer(serializers.ModelSerializer):
    """Сериализатор для АПИ соц сетей"""
    class Meta:
        model = AddSocialNetworks
        fields = ['icon_for_url', 'url_social_network', 'image']

class SubscribeSocialNetworksModelSerializer(serializers.ModelSerializer):
    """Сериализатор для главного  АПИ на ссылки соц.сетей"""
    social_networks = AddSocialNetworksSerializer(many=True)
    class Meta:
        model = SubscribeSocialNetworksModel
        fields = ['title', 'title2', 'social_networks']
