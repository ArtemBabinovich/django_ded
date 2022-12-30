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

    class Meta:
        verbose_name = 'Текст №1 для баннера № 2'
        verbose_name_plural = 'Текст №1 для баннера № 2'

    def __str__(self):
        return self.text


class Title2ForBanner2(models.Model):
    """Текст №1 для баннера № 2"""
    text = models.TextField('Текст №2 для баннера № 2')

    class Meta:
        verbose_name = 'Текст №2 для баннера № 2'
        verbose_name_plural = 'Текст №2 для баннера № 2'

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

    class Meta:
        verbose_name = 'Текст №1 для баннера № 4'
        verbose_name_plural = 'Текст №1 для баннера № 4'

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
    name = models.CharField(verbose_name='Название', max_length=50)
    item_number = models.IntegerField(verbose_name='Номер позиции в слайдере')
    foto = models.ImageField(verbose_name='Изображение для баннера',
                             upload_to='static/img/banner1', null=True, blank=True)

    class Meta:
        verbose_name = 'Наполнение слайдеров для баннеров'
        verbose_name_plural = 'Наполнения слайдеров для баннеров'
        ordering = ['item_number', 'name']

    def __str__(self):
        return self.name

class ModuleForMainPage(models.Model):
    """Модуль для главной страницы"""
    number_slot_bunner_1 = models.IntegerField(verbose_name='Номер слота баннера №1', null=True, blank=True)
    banner_type_1 = models.ForeignKey(Banner1, on_delete=models.SET_NULL, verbose_name='Выбор баннера типа №1', null=True, blank=True)
    number_slot_bunner_2 = models.IntegerField(verbose_name='Номер слота баннера №2', null=True, blank=True)
    banner_type_2 = models.ForeignKey(Banner2, on_delete=models.SET_NULL, verbose_name='Выбор баннера типа №2', null=True, blank=True)
    number_slot_bunner_3 = models.IntegerField(verbose_name='Номер слота баннера №3', null=True, blank=True)
    banner_type_3 = models.ForeignKey(Banner3, on_delete=models.SET_NULL, verbose_name='Выбор баннера типа №3', null=True, blank=True)
    number_slot_bunner_4 = models.IntegerField(verbose_name='Номер слота баннера №4', null=True, blank=True)
    banner_type_4 = models.ForeignKey(Banner4, on_delete=models.SET_NULL, verbose_name='Выбор баннера типа №4', null=True, blank=True)
    number_slot_bunner_5 = models.IntegerField(verbose_name='Номер слота баннера №5', null=True, blank=True)
    banner_type_5 = models.ForeignKey(Banner5, on_delete=models.SET_NULL, verbose_name='Выбор баннера типа №5', null=True, blank=True)

    class Meta:
        verbose_name = 'Модуль для главной страницы'
        verbose_name_plural = 'Модуль для главной страницы'
        unique_together = ['number_slot_bunner_1', 'number_slot_bunner_2', 'number_slot_bunner_3',]
#
    def __str__(self):
        return 'Модуль для главной страницы'


