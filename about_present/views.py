from rest_framework import viewsets, mixins
from rest_framework.response import Response

from .models import AboutPresent, Recipient, Reason, Present, RemindForDays
from .serializers import AboutPresentSerializer, RecipientSerializer, ReasonSerializer,\
    PresentSerializer, RemindForDaysSerializer


class  RecipientViewSets(mixins.ListModelMixin, viewsets.GenericViewSet):
    """API  всех  получателей подарка"""
    queryset = Recipient.objects.all()
    serializer_class = RecipientSerializer


class  ReasonViewSets(mixins.ListModelMixin, viewsets.GenericViewSet):
    """API  получения всех  событий для  подарка"""
    queryset = Reason.objects.all()
    serializer_class = ReasonSerializer


class  PresentViewSets(mixins.ListModelMixin, viewsets.GenericViewSet):
    """API для получения типов подарка"""
    queryset = Present.objects.all()
    serializer_class = PresentSerializer


class  RemindForDaysViewSets(mixins.ListModelMixin, viewsets.GenericViewSet):
    """API для получения всех дат напоминания"""
    queryset = RemindForDays.objects.all()
    serializer_class = RemindForDaysSerializer


class AboutPresentAdd(viewsets.ViewSet):
    """API для оформления подарка"""
    queryset = AboutPresent.objects.all()

    def create(self, request):
        serializer = AboutPresentSerializer(data=request.data)
        if serializer.is_valid():
            response = serializer.save(validated_data=serializer.validated_data)
            return Response(AboutPresentSerializer(response).data)
        else:
            return Response(serializer.errors)
