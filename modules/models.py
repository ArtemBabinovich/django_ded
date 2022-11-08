from datetime import datetime

from colorfield.fields import ColorField
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
from tinymce import models as tinymce_models
from django.db import models


def validate_current_century(value):
    """Валидатор для выбора года в каллендаре баннера,
       максимальное значение 2050"""
    if value.year > 2050:
        raise ValidationError('Год не может превышать значение 2050')


class FotoForBanner(models.Model):
    """Добовление фотографии, текста и позиции для слайдера в баннере"""
    name = models.CharField('Название', max_length=50)
    item_number = models.IntegerField('Номер позиции в слайдере')
    foto = models.ImageField(verbose_name='Изображение для баннера',
                             upload_to='static/img/banner1', null=True, blank=True)
    text = tinymce_models.HTMLField(verbose_name='Текст', null=True, blank=True, default=None)

    class Meta:
        verbose_name = 'Наполнение слайдеров для баннеров'
        verbose_name_plural = 'Наполнения слайдеров для баннеров'
        ordering = ['item_number', 'name']

    def __str__(self):
        return self.name


class Calendar(models.Model):
    """Выбор даты для каллендаря"""
    banner_calendar = models.DateField(validators=[validate_current_century])

    class Meta:
        verbose_name = 'Каллендарь'
        verbose_name_plural = 'Каллендарь'

    def __str__(self):
        return str(self.banner_calendar)


class Timer(models.Model):
    """Таймеры для баннеров"""
    name = models.CharField('Название', max_length=50)
    text = tinymce_models.HTMLField(verbose_name='Текст', null=True, blank=True)
    timer_days = models.IntegerField('Таймер - дни', default=0)  # Таймер
    timer_hours = models.IntegerField('Таймер - часы', default=0,
                                      validators=[MaxValueValidator(24)])
    timer_minutes = models.IntegerField('Таймер - минуты', default=0,
                                        validators=[MaxValueValidator(60)])
    timer_seconds = models.IntegerField('Таймер - секунды', default=0,
                                        validators=[MaxValueValidator(60)])

    class Meta:
        verbose_name = 'Таймер'
        verbose_name_plural = 'Таймеры'

    def __str__(self):
        return self.name


class Banner(models.Model):
    """Рекламные Баннера"""
    slider_type_choice = (
        ('horizontal', 'Горизонтальный'),
        ('vertical', 'Вертикальный'),
    )
    name = models.CharField('Название баннера', max_length=250)
    calendar = models.ForeignKey(Calendar, on_delete=models.SET(datetime.today().strftime("%Y-%m-%d")),
                                 null=True, blank=True, verbose_name='Каллендарь')
    slider_type = models.CharField('Тип слайдера',max_length=50, choices=slider_type_choice)
    slider_fotos = models.ManyToManyField('FotoForBanner', verbose_name='Выбрать фото для слайдера')
    slider_speed = models.IntegerField('Скорость переключения слайдера в сек.', default=2)
    foto_count = models.IntegerField('Счетчик фото', default=10, null=True, blank=True)
    timer = models.ForeignKey(Timer, verbose_name='Таймер', on_delete=models.SET_NULL, null=True, blank=True)
    url = models.CharField('Внутренняя ссылка', max_length=50)
    text = tinymce_models.HTMLField(verbose_name='Текст', null=True, blank=True)

    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннера'

    def __str__(self):
        return self.name


class Module(models.Model):
    name = models.CharField('Название модуля', max_length=250)
    slot_1 = models.ForeignKey(Banner, on_delete=models.SET_NULL, null=True, blank=True, related_name='slot_1')
    slot_2 = models.ForeignKey(Banner, on_delete=models.SET_NULL, null=True, blank=True, related_name='slot_2')
    slot_3 = models.ForeignKey(Banner, on_delete=models.SET_NULL, null=True, blank=True, related_name='slot_3')
    slot_4 = models.ForeignKey(Banner, on_delete=models.SET_NULL, null=True, blank=True, related_name='slot_4')
    slot_5 = models.ForeignKey(Banner, on_delete=models.SET_NULL, null=True, blank=True, related_name='slot_5')

    class Meta:
        verbose_name = 'Модуль'
        verbose_name_plural = 'Модули'

    def __str__(self):
        return self.name


