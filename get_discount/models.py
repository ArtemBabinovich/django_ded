from django.core.validators import RegexValidator
from django.db import models


class GetDiscount(models.Model):
    """Модель оформления заявки на скидку"""
    name = models.CharField('Имя отправителя', max_length=50)
    phone = models.CharField('Телефон отправителя', max_length=18, validators=[RegexValidator(regex=r'^[-0-9+() ]{11,18}$',
                                                        message='Поле должно состоять из цифр или знаков + () -')])
    email = models.EmailField('Почта отправителя')
    friends_name = models.CharField('Имя друга',max_length=50)
    friends_phone = models.CharField('Телефон друга', max_length=18, validators=[RegexValidator(regex=r'^[-0-9+() ]{11,18}$',
                                                        message='Поле должно состоять из цифр или знаков + () -')])
    friends_email = models.EmailField('Почта друга')

    class Meta:
        verbose_name = 'Оформление заявки на скидку'
        verbose_name_plural = 'Оформление заявки на скидку'


    def __str__(self):
        return f"Отправитель {self.name} {self.phone}"

# Create your models here.
