from django.db import transaction
from rest_framework import serializers

from .models import Recipient, Reason, Present, Date, \
    RemindForDays, AboutPresent, OnlyGetAboutPresent


class RecipientSerializer(serializers.ModelSerializer):
    """Сериализатор для получателя подарка"""

    class Meta:
        model = Recipient
        fields = ['id', 'name']


class ReasonSerializer(serializers.ModelSerializer):
    """Сериализатор для повода подарка"""

    class Meta:
        model = Reason
        fields = ['id', 'name']


class PresentSerializer(serializers.ModelSerializer):
    """Сериализатор типа подарка"""

    class Meta:
        model = Present
        fields = ['id', 'name']


class DateSerializer(serializers.ModelSerializer):
    """Сериализатор для даты события"""

    class Meta:
        model = Date
        fields = ['date']


class RemindForDaysSerializer(serializers.ModelSerializer):
    """Сериализатор для даты напоминания"""

    class Meta:
        model = RemindForDays
        fields = ['id', 'days']


class AboutPresentSerializer(serializers.ModelSerializer):
    """Сериализатор для оформления подарка"""
    about_present = DateSerializer(many=True)
    recipient = serializers.PrimaryKeyRelatedField(queryset=Recipient.objects.all())
    reason = serializers.PrimaryKeyRelatedField(queryset=Reason.objects.all())
    present = serializers.PrimaryKeyRelatedField(queryset=Present.objects.all())
    remind_for_days = serializers.PrimaryKeyRelatedField(queryset=RemindForDays.objects.all())
    remind_every_years = serializers.BooleanField()

    class Meta:
        model = AboutPresent
        fields = ['id', 'name', 'email', 'phone', 'about_present', 'recipient',
                  'reason', 'present', 'remind_for_days', 'remind_every_years']

    # def validated_date
    def validate_dates(self, value):

        if len(value) < 1:
            raise serializers.ValidationError({"error": "Выберите дату события"})
        else:
            return value

    def save(self, validated_data):

        with transaction.atomic():
            present = AboutPresent(name=validated_data['name'], email=validated_data['email'],
                                   phone=validated_data['phone'], recipient=validated_data['recipient'],
                                   reason=validated_data['reason'], present=validated_data['present'],
                                   remind_for_days=validated_data['remind_for_days'],
                                   remind_every_years=validated_data['remind_every_years'],)
            present.save()
            for value in validated_data['about_present']:
                date = Date(date=value.get("date"))
                date.save()
                present.about_present.add(date.id)
        return present


class OnlyReadAboutPresentSerializer(serializers.ModelSerializer):
    """Сериализатор на API View оформления подарков"""
    recipient_set = RecipientSerializer(many=True)
    reason_set = ReasonSerializer(many=True)
    present_set = PresentSerializer(many=True)
    remindfordays_set = RemindForDaysSerializer(many=True)

    class Meta:
        model = OnlyGetAboutPresent
        fields = ['reason_set', 'recipient_set', 'present_set', 'remindfordays_set']
