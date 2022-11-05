from ckeditor.fields import RichTextField
from colorfield.fields import ColorField
from django.db import models



# отдавать отдельным файлов в json или привязывать к количеству отдаваемых
# записей отсортированные записи по определённому полю, к примеру is_active
class CountServicesCatalog(models.Model):
    """Количество тематических модулей"""
    count_modules = models.PositiveIntegerField('Количество ТЕМ', blank=True, default=0)

    class Meta:
        verbose_name = 'Количество ТЕМ'
        verbose_name_plural = 'Количество ТЕМ'

    def __str__(self):
        return self.count_modules


class ServiceCatalog(models.Model):
    """Kаталог УСЛУГ"""
    catalog_title = models.CharField('Заголовок ТЕМЫ', max_length=255)
    color_title = ColorField('Цвет заголовка', format='hexa')
    is_active = models.BooleanField(default=False)
    service_position = models.OneToOneField('ServiceCatalogPosition', on_delete=models.CASCADE, verbose_name='Позиция')
    # вопрос по количеству тем, как их выводить и как связывать
    count = models.ForeignKey('CountServicesCatalog',
                              on_delete=models.SET_NULL,
                              verbose_name='Количество ТЕМ',
                              blank=True,
                              null=True,
                              default=None)

    class Meta:
        verbose_name = 'Каталог УСЛУГ'
        verbose_name_plural = 'Каталог УСЛУГ'

    def __str__(self):
        return self.catalog_title


class ServiceCatalogPosition(models.Model):
    """Порядковый номер КАТАЛОГА"""
    number_position = models.PositiveIntegerField('Номер позиции', blank=True, default=1)

    class Meta:
        verbose_name = 'Позиция КАТАЛОГА'
        verbose_name_plural = 'Позиции КАТАЛОГОВ'

    def __str__(self):
        return self.number_position


class ChapterCatalog(models.Model):
    """Раздел УСЛУГ"""
    chapter_title = models.CharField('Название РАЗДЕЛА', max_length=128)
    is_active = models.BooleanField('Активная', default=False)
    service_catalog = models.ForeignKey(ServiceCatalog,
                                        on_delete=models.SET_NULL,
                                        default=None,
                                        blank=True,
                                        null=True,
                                        verbose_name='Тема')
    position = models.OneToOneField('ChapterPosition', on_delete=models.CASCADE, verbose_name='Позиция РАЗДЕЛА')
    """
    Вовка, свяжи Баннер и удали комменты, так же рассудить у какой модели будет происходить прикручивание БАННЕРА,
    Услуга или Раздел могут выбирать свой БАННЕР или сам БАННЕР выбирает какие услуги или разделы будут у него
    """
    #banner = models.ManyToManyField('Вовка свяжи БАННЕР', verbose_name='Баннер')

    class Meta:
        verbose_name = 'Позиция в каталоге'
        verbose_name_plural = 'Позиция в каталоге'

    def __str__(self):
        return self.chapter_title


class ChapterPosition(models.Model):
    """порядковый номер позиции РАЗДЕЛА"""
    number_position = models.PositiveIntegerField('Позиция в каталоге', blank=True, default=1)

    class Meta:
        verbose_name = 'Позиция в каталоге'
        verbose_name_plural = 'Позиция в каталоге'
        ordering = ['number_position']

    def __str__(self):
        return self.number_position


class Service(models.Model):
    """УСЛУГА"""
    MARKER_SERVICES = [
        ('hit', 'ХИТ'),
        ('top', 'ТОП'),
        ('new', 'NEW'),
        ('stock', 'АКЦИЯ'),
    ]
    service_title = models.CharField('Название услуги', max_length=255)
    marker = models.CharField('Маркер услуги', max_length=5, choices=MARKER_SERVICES, blank=True, null=True)
    services_catalog = models.ForeignKey(ChapterCatalog,
                                         on_delete=models.SET_NULL,
                                         default=None,
                                         blank=True,
                                         null=True,
                                         verbose_name='Каталог')
    active = models.BooleanField('Активная', default=False)
    position_service = models.OneToOneField('PositionServices', on_delete=models.CASCADE, verbose_name='Позиция УСЛУГИ')
    """
    Вовка, свяжи Баннер и удали комменты, так же рассудить у какой модели будет происходить прикручивание БАННЕРА,
    Услуга или Раздел могут выбирать свой БАННЕР или сам БАННЕР выбирает какие услуги или разделы будут у него
    """
    #banner = models.ManyToManyField('Вовка свяжи БАННЕР', verbose_name='Баннер')

    class Meta:
        verbose_name = 'УСЛУГА'
        verbose_name_plural = 'УСЛУГИ'

    def __str__(self):
        return self.service_title


class PositionServices(models.Model):
    """Позиция в очереди"""
    number_position = models.PositiveIntegerField('Номер позиции', blank=True, default=1)

    class Meta:
        verbose_name = 'Номер очереди'
        verbose_name_plural = 'Номер очереди'
        ordering = ['number_position']

    def __str__(self):
        return self.number_position


class DetailServer(models.Model):
    """Детализация для фотослайдера"""
    title = models.CharField(max_length=128)
    image = models.ImageField('Изображение', upload_to='services/static/services/main_photo/')
    short_descriptions = models.CharField('Доп. описание', max_length=128, blank=True, null=True)
    active = models.BooleanField('Активная', default=True)
    adult_content = models.BooleanField('18+', default=False)
    position_service = models.OneToOneField('PositionDetailService',
                                            on_delete=models.CASCADE,
                                            verbose_name='Позиция УСЛУГИ')
    modul_text = models.ForeignKey('TextDetailService',
                                   on_delete=models.SET_NULL,
                                   default=None,
                                   blank=True,
                                   null=True,
                                   verbose_name='Какой текст вставить')

    class Meta:
        verbose_name = 'Слайдер УСЛУГ'
        verbose_name_plural = 'Слайдер УСЛУГ'

    def __str__(self):
        return self.title


class PositionDetailService(models.Model):
    """Порядковый номер позиции УСЛУГИ"""
    number_position = models.PositiveIntegerField('Номер позиции', blank=True, default=1)

    class Meta:
        verbose_name = 'Номер очереди'
        verbose_name_plural = 'Номер очереди'
        ordering = ['number_position']

    def __str__(self):
        return self.number_position


class TextDetailService(models.Model):
    """Модуль СОДЕРЖАНИЕ(при расскрытии читать советы)"""
    # ЗАголовок и подзаголовок страницастраница 63 пункт 37.6, страница 51(схемы) есть неясности,
    # плюс макет не соответсвует ТЗ
    main_header = models.CharField('Заголовок', max_length=255)
    subtitle = models.CharField('Подзаголовок', max_length=255)
    text_author = models.OneToOneField('AuthorText',
                                       on_delete=models.SET_NULL,
                                       default=None,
                                       blank=True,
                                       null=True,
                                       verbose_name='Прикепить статью автора')
    photo_gallery = models.ManyToManyField('ImageForTextDetailService', verbose_name='Фотографии')
    discount = models.ForeignKey('PromotionsDiscounts',
                                 on_delete=models.SET_NULL,
                                 default=None,
                                 blank=True,
                                 null=True,
                                 verbose_name='Прикрепить акцию')

    class Meta:
        verbose_name = 'СОДЕРЖАНИЕ'
        verbose_name_plural = 'СОДЕРЖАНИЕ'

    def __str__(self):
        return self.main_header


class PromotionsDiscounts(models.Model):
    """Модуль акции, для прикручивания к содержанию"""
    text = RichTextField()

    class Meta:
        verbose_name = 'АКЦИЯ'
        verbose_name_plural = 'АКЦИИ'

    def __str__(self):
        return 'Акция'


class AuthorText(models.Model):
    """Текст АВТОРА"""
    text_author = RichTextField()
    position_job = models.CharField(max_length=128, verbose_name='Должность')
    photo_author = models.ImageField('Фтография автора статьи', upload_to='services/static/services/photo_author')

    class Meta:
        verbose_name = 'Текст АВТОРА'
        verbose_name_plural = 'Текст АВТОРА'

    def __str__(self):
        return 'Текст Автора'


class ImageForTextDetailService(models.Model):
    """Фотогалерея СОДЕРЖАНИЯ"""
    image = models.ImageField('Фотографии для услуги', upload_to='services/static/services/other_photo/')
    image_title = models.CharField('Заголовок фотографии', blank=True, null=False, default='', max_length=128)
    is_active = models.BooleanField('Активная', default=False)

    class Meta:
        verbose_name = 'Фотографии для СОДЕРЖАНИЯ'
        verbose_name_plural = 'Фотографии для СОДЕРЖАНИЯ'

    def __str__(self):
        return ''
