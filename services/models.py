from django.db import models


class ServiceCatalog(models.Model):
    '''каталог услуг'''
    title = models.CharField('Каталог', max_length=128, unique=True)
    image = models.ImageField('Изображение', upload_to='services/static/service_catalog/')
    # image_title = models.CharField('Заголовок фотографии', max_length=128)
    add_descriptions = models.CharField('Добавить описание', max_length=128, blank=True, null=True)

    class Meta:
        verbose_name = 'Каталог'
        verbose_name_plural = 'Каталог'

    def __str__(self):
        return self.title


class Service(models.Model):
    '''Конкретные услуги'''
    MARKER_SERVICES = [
        (None, 'Пусто'),
        ('hit', 'ХИТ'),
        ('top', 'ТОП'),
        ('new', 'NEW'),
        ('stock', 'АКЦИЯ'),
    ]
    # id_services = models.PositiveIntegerField(unique=True, auto_created=True)
    title = models.CharField('Название услуги', max_length=255)
    image = models.ImageField('Изображение', upload_to='services/static/services/main_photo/')
    image_title = models.CharField('Заголовок фотографии', max_length=128)
    short_descriptions = models.CharField('Доп. описание', max_length=128)
    # second_descriptions = models.CharField('Второе описание', max_length=128)
    price = models.CharField('Цена', max_length=128, blank=True, null=True)
    marker = models.CharField('Маркер услуги', max_length=10, choices=MARKER_SERVICES, blank=False, default='None')
    services_catalog = models.ForeignKey(ServiceCatalog, on_delete=models.CASCADE, verbose_name='Каталог')
    active = models.BooleanField('Активная', default=True)
    sort_service = models.PositiveIntegerField('Сортировка по номеру',
                                               blank=True,
                                               default=1,
                                               help_text='необязательное поле')

    class Meta:
        verbose_name = 'УСЛУГА'
        verbose_name_plural = 'УСЛУГИ'
        ordering = ('sort_service', 'title', 'marker',)

    def __str__(self):
        return self.title


class FullDescriptionsService(models.Model):
    '''Деетальное описание'''
    descriptions = models.TextField('Описание', default='')


class ImageForServices(models.Model):
    """Фотогалерея"""
    image = models.ImageField('Фотографии для услуги', upload_to='services/static/services/other_photo/')
    image_title = models.CharField('Заголовок фотографии', blank=True, null=False, default='', max_length=128)
    services = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='Дополнительное фото')
    is_active = models.BooleanField('Активная', default=False)

    class Meta:
        verbose_name = 'Фотографии'
        verbose_name_plural = 'Фотографии'

    def __str__(self):
        return ''
