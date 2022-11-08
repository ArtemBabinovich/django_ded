from datetime import datetime

from colorfield.fields import ColorField
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
from django.db import models
from .choice import font_choice, slider_type_choice



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
                             upload_to='static/img/banner1')
    text = models.TextField('Текст')

    class Meta:
        verbose_name = 'Добавить изображение для баннера № 1'
        verbose_name_plural = 'Добавить изображения для баннера № 1'

    def __str__(self):
        return self.name


class Calendar(models.Model):
    """Выбор даты для каллендаря"""
    banner_calendar = models.DateField(validators=[validate_current_century])

    def __str__(self):
        return str(self.banner_calendar)


class Banner(models.Model): # Можно ли так называть класс?
    """Рекламные Баннера"""
    name = models.CharField('Название баннера', max_length=250)
    calendar = models.ForeignKey(Calendar, on_delete=models.SET(datetime.today().strftime("%Y-%m-%d")),
                                 null=True, blank=True, verbose_name='Каллендарь')
    slider_type = models.CharField('Тип слайдера',max_length=50, choices=slider_type_choice)
    slider_fotos = models.ManyToManyField('FotoForBanner', verbose_name='Выбрать фото для слайдера')
    slider_speed = models.IntegerField('Скорость переключения слайдера в сек.', default=2)
    foto_count = models.IntegerField('Счетчик фото', default=10) # Счетчик фото
    timer_days = models.IntegerField('Таймер - дни', default=0) # Таймер
    timer_hours = models.IntegerField('Таймер - часы', default=0,
                                      validators=[MaxValueValidator(24)])
    timer_minutes = models.IntegerField('Таймер - минуты', default=0,
                                        validators=[MaxValueValidator(60)])
    timer_seconds = models.IntegerField('Таймер - секунды', default=0,
                                        validators=[MaxValueValidator(60)])
    url = models.CharField('Внутренняя ссылка', max_length=2083) # Какая максимальная длина URL
    text = models.TextField('Текст')
    font_family = models.CharField('Шрифт', max_length=100, choices=font_choice)
    font_size = models.IntegerField('Размер шрифта', default=18) #Какие ограничения и кокой стандартный должен быть
    font_italic = models.BooleanField('Курсив', default=False)
    font_bold = models.BooleanField('Жирный', default=False)
    font_underline = models.BooleanField('Подчеркнутый', default=False)
    font_color = ColorField(default='#7FB7FF', verbose_name='Цвет шрифта')
    # Вопрос по растягиванию высоты модуля

    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннера'

    def __str__(self):
        return self.name



# Create your models here.
