from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from django.db import models

from services.models import ServicesCatalog, Services
from services.utils import slugify


class GeneralModel(models.Model):
    """Общаяя модель для Советов"""
    services_catalog = models.ForeignKey(ServicesCatalog,
                                         related_name='advices_for_services_catalog',
                                         verbose_name='К какому каталогу прикремить',
                                         on_delete=models.SET_NULL,
                                         null=True,
                                         blank=True)
    title = models.CharField('Название блока советов', max_length=128)
    advices = models.ManyToManyField('ModelTips',
                                     verbose_name='Какие советы добавить',
                                     # blank=True,
                                     related_name='general')

    class Meta:
        verbose_name = 'Сборка советов в одну API'
        verbose_name_plural = 'Сборка советов в одну API'

    def __str__(self):
        return self.title


class ModelTips(models.Model):
    """Модель советов"""
    title = models.CharField('Название совета', max_length=255)
    title2 = models.CharField('Дополнительное название', max_length=255, null=True, blank=True)
    content = models.ManyToManyField('ContentTips', verbose_name='Какое содержание советов прикрепить', blank=True)

    class Meta:
        verbose_name = 'Советы'
        verbose_name_plural = 'Советы'

    def __str__(self):
        return self.title


class ContentTips(models.Model):
    """Модель содержания советов"""
    title = models.CharField('Название содержания', max_length=128, unique=True)
    url = AutoSlugField(populate_from='title', unique=True, slugify=slugify)
    description = RichTextField(verbose_name='Описание')
    service = models.ForeignKey(Services,
                                on_delete=models.SET_NULL,
                                null=True,
                                blank=True,
                                verbose_name='Ссылка на УСЛУГУ')
    photo = models.ImageField('Фотография', upload_to='read_tips/static/img/photo_for_tips', null=True, blank=True)
    services_catalog = models.ForeignKey(ServicesCatalog,
                                         on_delete=models.SET_NULL,
                                         null=True,
                                         blank=True,
                                         verbose_name='На какой КАТАЛОГ ссылать фото')

    class Meta:
        verbose_name = 'Содержание СОВЕТОВ'
        verbose_name_plural = 'Содержание СОВЕТОВ'

    def __str__(self):
        return self.title


class PromotionsDiscounts(models.Model):
    """Модель акции, для прикручивания к содержанию"""
    title = models.CharField('Название акции', max_length=128)
    text = RichTextField('Описание акции')
    is_activ = models.BooleanField('Активная', default=False)
    general_model = models.OneToOneField(GeneralModel,
                                         related_name='discount',
                                         verbose_name='К какой Сборке советов прикрепить',
                                         on_delete=models.SET_NULL,
                                         null=True,
                                         blank=True)

    class Meta:
        verbose_name = 'АКЦИЯ'
        verbose_name_plural = 'АКЦИИ'

    def __str__(self):
        return self.title
