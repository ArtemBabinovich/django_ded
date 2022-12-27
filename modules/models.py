from datetime import datetime
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
from tinymce import models as tinymce_models
from django.db import models


def validate_current_century(value):
    """Валидатор для выбора года в каллендаре баннера,
       максимальное значение 2050"""
    if value.year > 2050:
        raise ValidationError('Год не может превышать значение 2050')

class Banner1(models.Model):
    """Баннер №1"""
    calendar_title = models.CharField('Заголовок календаря', max_length=100)
    calendar_date = models.DateField(validators=[validate_current_century], verbose_name='Выбор даты')
    text_title_1 = models.CharField('Заголовок №1', max_length=100)
    text_1 = models.TextField('Текст №1')
    slider = models.ManyToManyField('FotoForBanner', verbose_name='Выбрать фото для слайдера')
    text_title_2 = models.CharField('Заголовок №2', max_length=100)
    text_2 = models.TextField('Текст №2')
    discount_amount = models.IntegerField(verbose_name='Сумма скидки')
    timer_title = models.CharField('Заголовок таймера', max_length=100)
    timer = models.DateTimeField('Дата и время окончания таймера')
    banner_position = models.IntegerField(verbose_name='Порядковый номер баннера')

    class Meta:
        verbose_name = 'Баннер типа №1'
        verbose_name_plural = 'Баннера типа №1'

    def __str__(self):
        return f"Баннер №1, порядковый номер - {self.banner_position}"


class Title1ForBanner2(models.Model):
    """Текст №1 для баннера № 2"""
    text = models.TextField('Текст №1 для баннера № 2')

    def __str__(self):
        return self.text


class Title2ForBanner2(models.Model):
    """Текст №1 для баннера № 2"""
    text = models.TextField('Текст №2 для баннера № 2')

    def __str__(self):
        return self.text


class Banner2(models.Model):
    """Баннер №2"""
    calendar_title = models.CharField('Заголовок календаря', max_length=100)
    calendar_date = models.DateField(validators=[validate_current_century], verbose_name='Выбор даты')
    title = models.CharField('Заголовок', max_length=100)
    text = models.TextField('Текст')
    slider_1 = models.ManyToManyField('FotoForBanner', related_name='slider_1', verbose_name='Выбрать фото для слайдера №1')
    text_1 = models.ManyToManyField('Title1ForBanner2',verbose_name='Текстовое пространство №1')
    slider_2 = models.ManyToManyField('FotoForBanner', related_name='slider_2', verbose_name='Выбрать фото для слайдера №2')
    text_2 = models.ManyToManyField('Title2ForBanner2', verbose_name='Текстовое пространство №2')
    discount_amount = models.IntegerField(verbose_name='Сумма скидки')
    timer_title = models.CharField('Заголовок таймера', max_length=100)
    timer = models.DateTimeField('Дата и время окончания таймера')
    banner_position = models.IntegerField(verbose_name='Порядковый номер баннера')

    class Meta:
        verbose_name = 'Баннер типа №2'
        verbose_name_plural = 'Баннера типа №2'

    def __str__(self):
        return f"Баннер №2, порядковый номер - {self.banner_position}"


class Banner3(models.Model):
    """Баннер №3"""
    calendar_title = models.CharField('Заголовок календаря', max_length=100)
    calendar_date = models.DateField(validators=[validate_current_century], verbose_name='Выбор даты')
    title = models.CharField('Заголовок', max_length=100)
    slider = models.ManyToManyField('FotoForBanner', verbose_name='Выбрать фото для слайдера')
    text_title = models.CharField('Заголовок Текста', max_length=100)
    text = models.TextField('Текст')
    timer_title = models.CharField('Заголовок таймера', max_length=100)
    timer = models.DateTimeField('Дата и время окончания таймера')
    banner_position = models.IntegerField(verbose_name='Порядковый номер баннера')

    class Meta:
        verbose_name = 'Баннер типа №3'
        verbose_name_plural = 'Баннера типа №3'

    def __str__(self):
        return f"Баннер №3, порядковый номер - {self.banner_position}"


class TextForBanner4(models.Model):
    """Текст №1 для баннера № 2"""
    text = models.TextField('Текст для баннера № 4')

    def __str__(self):
        return self.text


class Banner4(models.Model):
    """Баннер №3"""
    banner_title = models.CharField('Заголовок баннера', max_length=100)
    title = models.CharField('Заголовок', max_length=100)
    slider = models.ManyToManyField('FotoForBanner', verbose_name='Выбрать фото для слайдера')
    text_title = models.CharField('Заголовок перед текстовым пространством', max_length=100)
    text = models.ManyToManyField('TextForBanner4', verbose_name='Текстовое пространство')
    banner_position = models.IntegerField(verbose_name='Порядковый номер баннера')

    class Meta:
        verbose_name = 'Баннер типа №4'
        verbose_name_plural = 'Баннера типа №4'

    def __str__(self):
        return f"Баннер №4, порядковый номер - {self.banner_position}"


class Banner5(models.Model):
    """Баннер №5"""
    banner_title = models.CharField('Заголовок баннера', max_length=100)
    title = models.CharField('Заголовок', max_length=100)
    slider = models.ManyToManyField('FotoForBanner', verbose_name='Выбрать фото для слайдера')
    text_title = models.CharField('Заголовок перед текстовым пространством', max_length=100)
    text = models.TextField('Текст')
    discount_amount = models.IntegerField(verbose_name='Сумма скидки')
    banner_position = models.IntegerField(verbose_name='Порядковый номер баннера')

    class Meta:
        verbose_name = 'Баннер типа №5'
        verbose_name_plural = 'Баннера типа №5'

    def __str__(self):
        return f"Баннер №5, порядковый номер - {self.banner_position}"




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

# class Module(models.Model):
#     name = models.CharField('Название модуля', max_length=250)
#     slot_1 = models.ForeignKey(Banner, on_delete=models.SET_NULL, null=True, blank=True, related_name='slot_1')
#     slot_2 = models.ForeignKey(Banner, on_delete=models.SET_NULL, null=True, blank=True, related_name='slot_2')
#     slot_3 = models.ForeignKey(Banner, on_delete=models.SET_NULL, null=True, blank=True, related_name='slot_3')
#     slot_4 = models.ForeignKey(Banner, on_delete=models.SET_NULL, null=True, blank=True, related_name='slot_4')
#     slot_5 = models.ForeignKey(Banner, on_delete=models.SET_NULL, null=True, blank=True, related_name='slot_5')
#
#     class Meta:
#         verbose_name = 'Модуль'
#         verbose_name_plural = 'Модули'
#
#     def __str__(self):
#         return self.name


