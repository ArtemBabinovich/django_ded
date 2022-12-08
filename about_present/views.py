from django.db.models import Prefetch
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.response import Response

from .models import AboutPresent, Recipient, Reason, Present, RemindForDays, OnlyGetAboutPresent
from .serializers import AboutPresentSerializer, OnlyReadAboutPresentSerializer
from .tasks import send, send_to_telegram


class FullApiInfoViewSets(viewsets.ReadOnlyModelViewSet):
    """API для оформления подарков"""
    queryset = OnlyGetAboutPresent.objects.all() \
        .prefetch_related(Prefetch('recipient_set', queryset=Recipient.objects.all())) \
        .prefetch_related(Prefetch('reason_set', queryset=Reason.objects.all())) \
        .prefetch_related(Prefetch('present_set', queryset=Present.objects.all())) \
        .prefetch_related(Prefetch('remindfordays_set', queryset=RemindForDays.objects.all()))
    serializer_class = OnlyReadAboutPresentSerializer


#
# class RecipientViewSets(mixins.ListModelMixin, viewsets.GenericViewSet):
#     """API  всех  получателей подарка"""
#     queryset = Recipient.objects.all()
#     serializer_class = RecipientSerializer
#
#
# class ReasonViewSets(mixins.ListModelMixin, viewsets.GenericViewSet):
#     """API  получения всех  событий для  подарка"""
#     queryset = Reason.objects.all()
#     serializer_class = ReasonSerializer
#
#
# class PresentViewSets(mixins.ListModelMixin, viewsets.GenericViewSet):
#     """API для получения типов подарка"""
#     queryset = Present.objects.all()
#     serializer_class = PresentSerializer
#
#
# class RemindForDaysViewSets(mixins.ListModelMixin, viewsets.GenericViewSet):
#     """API для получения всех дат напоминания"""
#     queryset = RemindForDays.objects.all()
#     serializer_class = RemindForDaysSerializer


class AboutPresentAdd(viewsets.ViewSet):
    """API для оформления подарка"""
    queryset = AboutPresent.objects.all()

    @swagger_auto_schema(request_body=AboutPresentSerializer)
    def create(self, request):

        serializer = AboutPresentSerializer(data=request.data)
        if serializer.is_valid():
            response = serializer.save(validated_data=serializer.validated_data)
            # отправка письма на email при заказе
            send.delay(response.email, response.name, response.recipient)
            # отправка на бота
            send_to_telegram.delay(response.id)
            return Response(AboutPresentSerializer(response).data)
        else:
            return Response(serializer.errors)
