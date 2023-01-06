from autoslug import AutoSlugField
from colorfield.fields import ColorField
from django.db import models
from django.template.defaultfilters import slugify as dj_slugify

# преобразование кириллицы в Англ.
alphabet = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
            'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
            'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'i', 'э': 'e', 'ю': 'yu',
            'я': 'ya'}


def slugify(some_text):
    """Транскрипция slug с кириллицы на англ алфавит, проверка на уникальность URL"""
    return dj_slugify(''.join(alphabet.get(word, word) for word in some_text.lower()))


class ServicesCatalog(models.Model):
    """РАЗДЕЛ УСЛУГ 1-ая ветка дерева и большой ФОТОСЛАЙДЕР"""
    title = models.CharField('Заголовок РАЗДЕЛА УСЛУГ', max_length=255)
    additional_title = models.CharField('Допоплнительный заголовок', max_length=128, blank=True, null=True)
    additional_title_2 = models.CharField('Дополнительное описание', max_length=128, blank=True, null=True)
    image_for_big_slider = models.ImageField('Фотография большого слайдера',
                                             upload_to='services/static/img/foto_big_slider')
    color_title = ColorField('Цвет заголовка', format='hexa', default='#FFFFFFFF')
    is_active = models.BooleanField('Активня', default=True)
    url = AutoSlugField(populate_from='title', unique=True, slugify=slugify)
    # time_pause_for_mini_slider = models.PositiveIntegerField('Время для слайда "мини_слайдера',
    #                                                          default=4000,
    #                                                          blank=True)
    position = models.OneToOneField('ServicesCatalogPosition',
                                    on_delete=models.CASCADE,
                                    verbose_name='Номер очереди',
                                    null=True,
                                    blank=True,
                                    default=None)
    """
    Вовка, свяжи Баннер и удали комменты, так же рассудить у какой модели будет происходить прикручивание БАННЕРА,
    Услуга или Раздел могут выбирать свой БАННЕР или сам БАННЕР выбирает какие услуги или разделы будут у него
    """

    # banner = models.ForeignKey('Вовка свяжи БАННЕР', verbose_name='Баннер')

    class Meta:
        verbose_name = 'Создание КАТАЛОГА УСЛУГ'
        verbose_name_plural = 'Создание КАТАЛОГА УСЛУГ'
        ordering = ('position',)

    def __str__(self):
        if not self.additional_title:
            return self.title
        return f'{self.title} {self.additional_title}'


class ServicesCatalogPosition(models.Model):
    """Порядковый номер позиций РАЗДЕЛА УСЛУГ"""
    number_position = models.PositiveIntegerField('Позиция РАЗДЕЛА УСЛУГ',
                                                  blank=True,
                                                  null=True,
                                                  default=None,
                                                  unique=True)

    class Meta:
        verbose_name = 'Номер очереди'
        verbose_name_plural = 'Номер очереди'

    def __str__(self):
        return str(self.number_position)


class Services(models.Model):
    """УСЛУГА 2-ая ветка дерева и маленький ФОТОСЛАЙДЕР"""
    MARKER_SERVICES = [
        ('ХИТ', 'ХИТ'),
        ('ТОП', 'ТОП'),
        ('NEW', 'NEW'),
        ('АКЦИЯ', 'АКЦИЯ'),
    ]
    service_title = models.CharField('Название услуги', max_length=255)
    color_service_title = ColorField('Цвет названия услуги', format='hexa', default='#FFFFFFFF')
    marker = models.CharField('Маркер услуги', max_length=5, choices=MARKER_SERVICES, blank=True, null=True)
    image_for_mini_slider = models.ImageField('Фотография для маленького слайдера',
                                              upload_to='services/static/img/foto_mini_slider',
                                              default='',
                                              null=True,
                                              blank=True)
    bottom_description = models.CharField('Описание фотослайдера', max_length=128, blank=True, null=True)
    color_bottom_description = ColorField('Цвет описания', format='hexa', blank=True, null=True)
    bottom_description_2 = models.CharField('Доп. описание фотослайдера', max_length=128, blank=True, null=True)
    url = AutoSlugField(populate_from='service_title', unique=True, slugify=slugify)
    color_bottom_description_2 = ColorField('Цвет доп. описания', format='hexa', blank=True, null=True)
    service_catalog = models.ForeignKey(ServicesCatalog,
                                        related_name='services',
                                        on_delete=models.SET_NULL,
                                        default=None,
                                        blank=True,
                                        null=True,
                                        verbose_name='К какому РАЗДЕЛУ УСЛУГ отнести:')
    is_active = models.BooleanField('Активная', default=True)
    position_service = models.OneToOneField('PositionServices',
                                            on_delete=models.CASCADE,
                                            verbose_name='Номер очереди',
                                            null=True,
                                            blank=True,
                                            default=None)
    """
    Вовка, свяжи Баннер и удали комменты, так же рассудить у какой модели будет происходить прикручивание БАННЕРА,
    Услуга или Раздел могут выбирать свой БАННЕР или сам БАННЕР выбирает какие услуги или разделы будут у него
    """

    # banner = models.ForeignKey('Вовка свяжи БАННЕР', verbose_name='Баннер')

    class Meta:
        verbose_name = 'Создание УСЛУГ'
        verbose_name_plural = 'Создание УСЛУГ'
        ordering = ('position_service',)

    def __str__(self):
        return self.service_title


class PositionServices(models.Model):
    """Порядковый номер позиций УСЛУГ"""
    number_position = models.PositiveIntegerField('Позиция УСЛУГИ',
                                                  blank=True,
                                                  null=True,
                                                  default=None,
                                                  unique=True)

    class Meta:
        verbose_name = 'Номер очереди'
        verbose_name_plural = 'Номер очереди'

    def __str__(self):
        return str(self.number_position)
