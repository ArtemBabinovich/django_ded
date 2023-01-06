from django.db import transaction
from rest_framework import serializers

from ded import settings
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
    date = serializers.DateField(input_formats=settings.DATE_INPUT_FORMATS)

    class Meta:
        model = Date
        fields = ['date']


class RemindForDaysSerializer(serializers.ModelSerializer):
    """Сериализатор для даты напоминания"""

    class Meta:
        model = RemindForDays
        fields = ['id', 'days']


# TODO переделать поле days на стринг
class AboutPresentSerializer(serializers.ModelSerializer):
    """Сериализатор для оформления подарка"""
    # remind_for_days = serializers.
    about_present = DateSerializer(many=True)
    recipient = serializers.SlugRelatedField(slug_field='name', queryset=Recipient.objects.all())
    reason = serializers.SlugRelatedField(slug_field='name', queryset=Reason.objects.all())
    present = serializers.SlugRelatedField(slug_field='name', queryset=Present.objects.all())
    remind_for_days = serializers.SlugRelatedField(slug_field='days', queryset=RemindForDays.objects.all())
    # recipient = serializers.PrimaryKeyRelatedField(queryset=Recipient.objects.all())
    # reason = serializers.PrimaryKeyRelatedField(queryset=Reason.objects.all())
    # present = serializers.PrimaryKeyRelatedField(queryset=Present.objects.all())
    # remind_for_days = serializers.PrimaryKeyRelatedField(queryset=RemindForDays.objects.all())
    remind_every_years = serializers.BooleanField()

    class Meta:
        model = AboutPresent
        fields = ['id', 'name', 'email', 'phone', 'about_present',
                  'recipient', 'reason', 'present', 'remind_for_days',
                  'remind_every_years']

    def validate_dates(self, value):
        if len(value) < 1:
            raise serializers.ValidationError({"error": "Выберите дату события"})
        else:
            return value

    def save(self, validated_data):
        recipient = Recipient.objects.get(name=validated_data['recipient'].name)
        reason = Reason.objects.get(name=validated_data['reason'].name)
        present = Present.objects.get(name=validated_data['present'].name)
        remind_for_days = RemindForDays.objects.get(days=validated_data["remind_for_days"].days)
        with transaction.atomic():
            present = AboutPresent(name=validated_data['name'], email=validated_data['email'],
                                   phone=validated_data['phone'], recipient_id=recipient.id,
                                   reason_id=reason.id, present_id=present.id,
                                   remind_for_days_id=remind_for_days.id,
                                   remind_every_years=validated_data['remind_every_years'])

            present.save()

            for value in validated_data['about_present']:
                date = Date(date=value.get("date"), presents_id=present.id)
                date.save()
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
