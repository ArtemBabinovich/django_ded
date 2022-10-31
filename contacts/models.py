from colorfield.fields import ColorField
from django.core.validators import RegexValidator
from django.db import models


class SocialNetworks(models.Model):
    """Социальные сети"""
    logo = models.ImageField('Логотип социальной сети', upload_to='social_networks/image/')
    name = models.CharField('Название социальной сети', max_length=50)
    link = models.URLField('Ссылка на социальную сеть', max_length=255)

    class Meta:
        verbose_name = 'Социальная сети'
        verbose_name_plural = 'Социальные сети'

    def __str__(self):
        return self.name

class Phone(models.Model):
    "Телефонный номер"
    code = models.CharField('Код страны', max_length=2, default='+7',
                            validators=[RegexValidator(regex=r'\+7', message='Код должен быть равен "+7"')])
    number_operator = models.CharField('Код оператора', max_length=3,
                                          validators=[RegexValidator(regex=r'^\d{3}$', message='Код оператора должен состоять из 3 цифр')])
    number = models.CharField('Номер телефона', max_length=9,
                                          validators=[RegexValidator(regex=r'^\d{3}[-]?\d{2}[-]?\d{2}$',
                                                                     message='Код оператора должен состоять из 7 цифр')])
    color_number = ColorField(default='#FF0000', verbose_name='Цвет номера')

    class Meta:
        verbose_name = 'Телефонный номер'
        verbose_name_plural = 'Телефонные номера'

    def __str__(self):
        return (self.code + " " + str(self.number_operator) + " " + str(self.number))
