from django.db.models import Prefetch
from rest_framework import viewsets

from read_tips.models import GeneralModel, PromotionsDiscounts
from read_tips.serializers import MainSerializer
from services.models import ServicesCatalog


class ContentTips1ApiViewSets(viewsets.ReadOnlyModelViewSet):
    """API для читать СОВЕТЫ"""
    queryset = ServicesCatalog.objects.all() \
        .prefetch_related(Prefetch('advices_for_services_catalog', queryset=GeneralModel.objects.all()
                                   .prefetch_related(Prefetch('discount',
                                                              queryset=PromotionsDiscounts.objects.filter(
                                                                  is_activ=True)))))

    serializer_class = MainSerializer
    lookup_field = 'url'
