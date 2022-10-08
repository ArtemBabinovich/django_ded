import re
from django.core.exceptions import ValidationError
from django.db import models


class FotoSliderBase(models.Model):
    """Фотослайдер большой"""
    image = models.ImageField('Фотография для слайдера', upload_to='Base_slider/image/')
    text = models.CharField('Заголовок', max_length=34)

    class Meta:
        verbose_name = 'Главный Фотослайдер'
        verbose_name_plural = 'Главный Фотослайдер'

    def __str__(self):
        return self.text


class TimeSlideBase(models.Model):
    """Таймер времени паузы для фотослайдера"""
    time_pause = models.IntegerField('Таймер времени в секундах')

    class Meta:
        verbose_name = 'Таймер времени паузы для фотослайдера'
        verbose_name_plural = 'Таймер времени паузы для фотослайдеров'


"""ЛЕВАЯ ПАНЕЛЬ"""


class Position(models.Model):
    """Номер в списке"""
    number = models.IntegerField(verbose_name='Номер очереди', unique=True, default=True)

    class Meta:
        verbose_name = 'Номер в списке'
        verbose_name_plural = 'Номер в списке'

    def __str__(self):
        return f'{self.number}'


class Image(models.Model):
    """Фотографии"""
    image = models.ImageField(verbose_name='Фотографии', null=True, blank=True, upload_to='photos/')
    catalog_service = models.ForeignKey('CatalogService', verbose_name='Фотографии', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Фотографии'
        verbose_name_plural = 'Фотографии'

    def __str__(self):
        return ''


class Service(models.Model):
    """Раздел"""
    name = models.CharField(verbose_name='Раздел', max_length=250, unique=True)
    position = models.OneToOneField(Position, verbose_name='Номер', on_delete=models.CASCADE)
    is_active = models.BooleanField(verbose_name='Активен', default=True)

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Раздел'
        ordering = ['position']

    def __str__(self):
        return self.name

    def save(self, *args):
        limits = 10
        if Service.objects.count() < limits:
            super().save(*args)
        else:
            raise ValidationError('Слишком много записей в Разделе!')


class CatalogService(models.Model):
    """Услуги"""
    MARKER_CHOICES = (
        ('ХИТ', 'ХИТ',),
        ('ТОП', 'ТОП',),
        ('NEW', 'NEW',),
        ('АКЦИЯ', 'АКЦИЯ'),
    )
    name = models.CharField(verbose_name='Название', max_length=200, unique=True)
    marker = models.CharField(verbose_name='Маркер', max_length=200, choices=MARKER_CHOICES, blank=True, null=True)
    service = models.ForeignKey('Service', verbose_name='Раздел', on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    price = models.DecimalField(verbose_name='Цена', max_digits=8, decimal_places=2)
    position = models.OneToOneField(Position, verbose_name='Номер', on_delete=models.CASCADE)
    is_active = models.BooleanField(verbose_name='Активен', default=True)

    class Meta:
        verbose_name = 'Услуги'
        verbose_name_plural = 'Услуги'
        ordering = ['position']

    def __str__(self):
        return self.name


"""СЕРЕДИНА"""
