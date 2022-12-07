from django.db import transaction

from rest_framework import serializers

from .models import Recipient, Reason, Present, Date, \
    RemindForDays, AboutPresent


class RecipientSerializer(serializers.ModelSerializer):
    """Сериализатор для получателя подарка"""
    class Meta:
        model = Recipient
        fields = '__all__'


class ReasonSerializer(serializers.ModelSerializer):
    """Сериализатор для причины подарка"""
    class Meta:
        model = Reason
        fields = '__all__'


class PresentSerializer(serializers.ModelSerializer):
    """Сериализатор типа подарка"""
    class Meta:
        model = Present
        fields = '__all__'


class DateSerializer(serializers.ModelSerializer):
    """Сериализатор для даты события"""
    date = serializers.DateField(required=True)
    class Meta:
        model = Date
        fields = ['date']


class RemindForDaysSerializer(serializers.ModelSerializer):
    """Сериализатор для даты напоминания"""
    class Meta:
        model = RemindForDays
        fields = '__all__'


class AboutPresentSerializer(serializers.ModelSerializer):
    """Сериализатор для оформления подарка"""
    dates = DateSerializer(many=True)
    recipient = serializers.PrimaryKeyRelatedField(queryset=Recipient.objects.all())
    reason = serializers.PrimaryKeyRelatedField(queryset=Reason.objects.all())
    present = serializers.PrimaryKeyRelatedField(queryset=Present.objects.all())
    remind_for_days = serializers.PrimaryKeyRelatedField(queryset=RemindForDays.objects.all())
    remind_every_years = serializers.BooleanField()
    remind_every_day = serializers.BooleanField()
    class Meta:
        model = AboutPresent
        fields = ['id', 'name', 'email', 'phone', 'dates', 'recipient',
                  'reason', 'present', 'remind_for_days', 'remind_every_years', 'remind_every_day']

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
                                   remind_every_years=validated_data['remind_every_years'],
                                   remind_every_day=validated_data['remind_every_day'],)
            present.save()
            for value in validated_data['dates']:
                date = Date(date=value.get("date"))
                date.save()
                present.dates.add(date.id)
        return present


#TODO апиха на метод гет отдаёт( повод, кому,[что хотите заказать, напоминание за количество дней,]), метод пост напомнить о подарке, пост скидки 2+