from rest_framework import serializers

from social_networks.models import SubscribeSocialNetworksModel


class SubscribeSocialNetworksModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscribeSocialNetworksModel
        fields = ['title', 'title2', 'social_networks']
        depth = 1