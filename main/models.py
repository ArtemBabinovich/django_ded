from django.core.exceptions import ValidationError
from django.db import models
from adminsortable.models import SortableMixin
from adminsortable.fields import SortableForeignKey

"""КОНТАКТЫ"""


class Contact(models.Model):
    """Контакты"""
    maps = models.TextField(verbose_name='Расположение на карте', help_text='Ссылка с яндекс карты')
    attention_info = models.TextField(verbose_name='Опиание информации (ВНИМАНИЕ!)')
    photo_map = models.ImageField(verbose_name='Фотография (КАК ДОБРАТЬСЯ)', upload_to='contacts/')
    info_photo_map = models.TextField(verbose_name='Описание (КАК ДОБРАТЬСЯ)')
    photo_st = models.ImageField(verbose_name='Фотография (ВХОД В СТУДИЮ)', upload_to='contacts/')
    info_photo_st = models.TextField(verbose_name='Описание (ВХОД В СТУДИЮ)')
    address = models.CharField(verbose_name='Адрес', max_length=100, blank=True, null=True)
    website = models.CharField(verbose_name='Сайт', max_length=100, blank=True, null=True)
    email = models.CharField(verbose_name='E-mail', max_length=100, blank=True, null=True)
    skype = models.CharField(verbose_name='Skype', max_length=100, blank=True, null=True)
    phone1 = models.CharField(verbose_name='Телефон (Офис стационарный)', max_length=33, blank=True, null=True)
    phone2 = models.CharField(verbose_name='Телефон (Офис мобильный)', max_length=33, blank=True, null=True)
    phone3 = models.CharField(verbose_name='Телефон (Мобильный)', max_length=33, blank=True, null=True)

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return f'{self.address}'


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
    """Номер очереди"""
    number = models.PositiveIntegerField(verbose_name='Номер очереди', unique=True)

    class Meta:
        verbose_name = 'Номер очереди'
        verbose_name_plural = 'Номер очереди'
        ordering = ['number']

    def __str__(self):
        return f'{self.number}'


class Image(SortableMixin):
    """Фотографии"""
    category = SortableForeignKey('CatalogService', on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Фотографии', null=True, blank=True, upload_to='photos/')
    project_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    class Meta:
        verbose_name = 'Фотографии'
        verbose_name_plural = 'Фотографии'
        ordering = ['project_order']

    def __str__(self):
        return self.category.name


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
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    price = models.DecimalField(verbose_name='Цена', max_digits=8, decimal_places=2)
    is_active = models.BooleanField(verbose_name='Активен', default=True)

    class Meta:
        verbose_name = 'Услуги'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.name


class Gallery(models.Model):
    """Левая панель"""
    name = models.CharField(verbose_name='Раздел', max_length=250, unique=True)
    position = models.OneToOneField(Position, verbose_name='Номер очереди', on_delete=models.CASCADE)
    is_active = models.BooleanField(verbose_name='Активен', default=True)

    class Meta:
        verbose_name = 'Левая панель'
        verbose_name_plural = 'Левая панель'

    def __str__(self):
        return self.name


class GalleryImageRelation(SortableMixin):
    """Соединение и сортировка"""
    gallery = models.ForeignKey('Gallery', verbose_name='Раздел', on_delete=models.CASCADE)
    catalogsevice = SortableForeignKey('CatalogService', verbose_name='Услуги', on_delete=models.CASCADE)
    image_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    class Meta:
        verbose_name = 'Соединение и сортировка'
        verbose_name_plural = 'Соединение и сортировка'
        ordering = ['image_order']

    def __str__(self):
        return ''
