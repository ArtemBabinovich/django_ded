from django.core.exceptions import ValidationError
from django.db import models
from adminsortable.models import SortableMixin
from adminsortable.fields import SortableForeignKey

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
#
#
# """ЛЕВАЯ ПАНЕЛЬ"""
#
#
# class Position(models.Model):
#     """Номер очереди"""
#     number = models.PositiveIntegerField(verbose_name='Номер очереди', unique=True)
#
#     class Meta:
#         verbose_name = 'Номер очереди'
#         verbose_name_plural = 'Номер очереди'
#
#     def __str__(self):
#         return f'{self.number}'
#
#
# class Service(models.Model):
#     """Раздел"""
#     name = models.CharField(verbose_name='Раздел', max_length=250, unique=True)
#
#     position = models.OneToOneField(Position, verbose_name='Номер очереди', on_delete=models.CASCADE)
#     is_active = models.BooleanField(verbose_name='Активен', default=True)
#
#     class Meta:
#         verbose_name = 'Раздел'
#         verbose_name_plural = 'Раздел'
#         ordering = ['position']
#
#     def __str__(self):
#         return self.name
#
#     def save(self, *args):
#         limits = 10
#         if Service.objects.count() < limits:
#             super().save(*args)
#         else:
#             raise ValidationError('Слишком много записей в Разделе!')
#
#
# class Image(SortableMixin):
#     """Фотографии"""
#     category = SortableForeignKey('CatalogService', on_delete=models.CASCADE)
#     image = models.ImageField(verbose_name='Фотографии', null=True, blank=True, upload_to='photos/')
#     project_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
#
#     class Meta:
#         verbose_name = 'Фотографии'
#         verbose_name_plural = 'Фотографии'
#         ordering = ['project_order']
#
#     def __str__(self):
#         return self.category.name
#
#
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
    # service = models.ForeignKey('Service', verbose_name='Раздел', on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    price = models.DecimalField(verbose_name='Цена', max_digits=8, decimal_places=2)
    # position = models.OneToOneField('Position', verbose_name='Номер очереди', on_delete=models.CASCADE)
    is_active = models.BooleanField(verbose_name='Активен', default=True)

    class Meta:
        verbose_name = 'Услуги'
        verbose_name_plural = 'Услуги'
        # ordering = ['position']

    def __str__(self):
        return self.name


""""""
from django.db import models
from adminsortable.models import SortableMixin
from adminsortable.fields import SortableForeignKey


class Position(models.Model):
    """Номер очереди"""
    number = models.PositiveIntegerField(verbose_name='Номер очереди', unique=True)

    class Meta:
        verbose_name = 'Номер очереди'
        verbose_name_plural = 'Номер очереди'

    def __str__(self):
        return f'{self.number}'


class Section(models.Model):
    """Раздел"""
    name = models.CharField(verbose_name='Раздел', max_length=250, unique=True)
    position = models.OneToOneField(Position, verbose_name='Номер очереди', on_delete=models.CASCADE)
    is_active = models.BooleanField(verbose_name='Активен', default=True)

    class Meta:
        verbose_name = '- Раздел'
        verbose_name_plural = '- Раздел'
        ordering = ['position']

    def __str__(self):
        return self.name


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

class Gallery(models.Model):
    section = models.ForeignKey('Section', verbose_name='Раздел', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '- Панель'
        verbose_name_plural = '- панель'

    def __str__(self):
        return self.section.name


class GalleryImageRelation(SortableMixin):
    gallery = models.ForeignKey('Gallery', verbose_name="Gallery", on_delete=models.CASCADE)
    image = SortableForeignKey('CatalogService', verbose_name="Услуги", on_delete=models.CASCADE)
    image_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    class Meta:
        verbose_name = '- Услуги'
        verbose_name_plural = '- Услуги'
        ordering = ['image_order']

    def __str__(self):
        return ''
