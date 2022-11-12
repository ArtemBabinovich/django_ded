from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models

from modules.models import validate_current_century


class Recipient(models.Model):
    """Получатель подарка"""
    name = models.CharField('Получатель' ,max_length=50)

    class Meta:
        verbose_name = 'Получатель'
        verbose_name_plural = 'Получатели'

    def __str__(self):
        return self.name


class Reason(models.Model):
    """Причина подарка"""
    name = models.CharField('Причина', max_length=50)

    class Meta:
        verbose_name = 'Причина'
        verbose_name_plural = 'Причины'

    def __str__(self):
        return self.name


class Present(models.Model):
    """Тип подарка"""
    name = models.CharField('Подарок', max_length=50)

    class Meta:
        verbose_name = 'Подарок'
        verbose_name_plural = 'Подарки'

    def __str__(self):
        return self.name


class Date(models.Model):
    """Дата события для вручения подарка"""
    date = models.DateField(validators=[validate_current_century],  verbose_name='Дата события')

    class Meta:
        verbose_name = 'Дата получения'
        verbose_name_plural = 'Дата получения'

    def __str__(self):
        return str(self.date)


class RemindForDays(models.Model):
    """За какое кол-во дней напомнить"""
    days = models.IntegerField(verbose_name='За сколько дней напомнить')

    class Meta:
        verbose_name = 'За сколько дней напомнить'
        verbose_name_plural = 'За сколько дней напомнить'

    def __str__(self):
        return str(self.days)

class AboutPresent(models.Model):
    """Модель напоминания для вручения подарка"""
    name = models.CharField('Имя закзчика', max_length=50)
    email = models.EmailField('Почта заказчика')
    phone = models.CharField('Телефон заказчика', max_length=16, blank=True, null=True,
                             validators=[RegexValidator(regex=r'^[-0-9+() ]{11,18}$',
                                                        message='Поле должно состоять из цифр или знаков + () -')])
    dates = models.ManyToManyField(Date, verbose_name='Даты событий')
    recipient = models.ForeignKey(Recipient, on_delete=models.PROTECT, verbose_name='Кому')
    reason = models.ForeignKey(Reason, on_delete=models.PROTECT, verbose_name='Повод')
    present = models.ForeignKey(Present, on_delete=models.PROTECT, verbose_name='Подарок')
    remind_for_days = models.ForeignKey(RemindForDays, models.PROTECT, verbose_name='За сколько дней напомнить')
    remind_every_years = models.BooleanField(default=False, verbose_name='Напоминать ежегодно')
    date_created = models.DateField(auto_created=True, auto_now_add=True, verbose_name='Дата оформления')

    class Meta:
        verbose_name = 'Напомнить о подарках'
        verbose_name_plural = 'Напомнить о подарке'

    def __str__(self):
        return (f'{self.name} - {self.present.name}')



# Create your models here.
