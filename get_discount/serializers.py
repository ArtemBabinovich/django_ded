from rest_framework import serializers

from .models import GetDiscount


class GetDiscountSerializer(serializers.ModelSerializer):
    """Сериализатор для оформления заявки на скидку"""
    friends_phone = serializers.CharField(max_length=18, validators=[])
    class Meta:
        model = GetDiscount
        fields = '__all__'
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=GetDiscount.objects.all(),
                fields=('phone', 'friends_phone'),
                message="Поля имя отправителя и имя друга не могуг быть одинаковыми"
            ),
            serializers.UniqueTogetherValidator(
                queryset=GetDiscount.objects.all(),
                fields=('email', 'friends_email'),
                message="Поля почта отправителя и почта друга не могуг быть одинаковыми",

            )
        ]

    def save(self, validated_data):

        discount = GetDiscount(name=validated_data['name'], phone=validated_data['phone'],
                              email=validated_data['email'], friends_name=validated_data['friends_name'],
                              friends_phone=validated_data['friends_phone'],
                              friends_email=validated_data['friends_email'],
                              )
        discount.save()

        return discount
