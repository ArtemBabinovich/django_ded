from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, mixins
from rest_framework.response import Response

from .models import AboutPresent, Recipient, Reason, Present, RemindForDays
from .serializers import AboutPresentSerializer, RecipientSerializer, ReasonSerializer,\
    PresentSerializer, RemindForDaysSerializer
from .tasks import send_to_telegram



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
    @swagger_auto_schema(request_body=AboutPresentSerializer)
    def create(self, request):

        serializer = AboutPresentSerializer(data=request.data)
        if serializer.is_valid():
            response = serializer.save(validated_data=serializer.validated_data)
            send_to_telegram.delay(response.id)
            return Response(AboutPresentSerializer(response).data)
        else:
            return Response(serializer.errors)
