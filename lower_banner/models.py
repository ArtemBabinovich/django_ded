from django.dispatch import receiver
from django.db.models.signals import post_save, pre_delete, pre_save
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from django.db import models
from sortedm2m.fields import SortedManyToManyField

from modules.models import validate_current_century
from services.utils import slugify


class FotoForLowerBanner(models.Model):
    """Добовление фотографии,  и позиции для слайдера в нижнем баннере"""
    name = models.CharField(verbose_name='Название', max_length=50)
    item_number = models.IntegerField(verbose_name='Номер позиции в слайдере')
    foto = models.FileField(verbose_name='Изображение для баннера',
                             upload_to='img/low_banners', null=True, blank=True)

    class Meta:
        verbose_name = 'Наполнение слайдеров для баннеров'
        verbose_name_plural = 'Наполнения слайдеров для баннеров'
        ordering = ['item_number', 'name']

    def __str__(self):
        return self.name

class TextForLowerBanner(models.Model):
    """Текст ссылок для наполнения нижних баннеров"""
    title = models.CharField(max_length=100, verbose_name='Заголовок ссылки')
    text = RichTextField(verbose_name='Текст ссылки', null=True, blank=True, default=None)
    url = AutoSlugField(populate_from='title', unique=True, slugify=slugify)

    class Meta:

        verbose_name = 'Создать ссылку'
        verbose_name_plural = 'Создание ссылок'


    def __str__(self):
        return self.title

class LowerBanner1(models.Model):
    """Нижний Баннер №1"""
    slider = models.ManyToManyField('FotoForLowerBanner', verbose_name='Выбрать фото для слайдера',blank=True)
    link_block_1 = models.ManyToManyField(TextForLowerBanner, verbose_name='Блок ссылок №1', related_name='b1_link_1')
    link_block_2 = models.ManyToManyField(TextForLowerBanner, verbose_name='Блок ссылок №2', related_name='b1_link_2')
    link_block_3 = models.ManyToManyField(TextForLowerBanner, verbose_name='Блок ссылок №3', related_name='b1_link_3')
    calendar_date = models.DateField(validators=[validate_current_century], verbose_name='Выбор даты')
    timer = models.DateTimeField('Дата и время окончания таймера')
    position = models.IntegerField(verbose_name='Порядковый номер баннера')

    class Meta:
        verbose_name = 'Нижний Баннер типа №1'
        verbose_name_plural = 'Нижний Баннера типа №1'


    def __str__(self):
        return f"Нижний Баннер №1, порядковый номер - {self.position}"




class LowerBanner2(models.Model):
    """Нижний Баннер №2"""
    slider_1 = models.ManyToManyField('FotoForLowerBanner', verbose_name='Выбрать фото для слайдера', blank=True, related_name='b2_slider_1')
    link_block_1 = models.ManyToManyField(TextForLowerBanner, verbose_name='Блок ссылок №1', related_name='b2_link_1')
    link_block_2 = models.ManyToManyField(TextForLowerBanner, verbose_name='Блок ссылок №2', related_name='b2_link_2')
    slider_2 = models.ManyToManyField('FotoForLowerBanner', verbose_name='Выбрать фото для слайдера', blank=True, related_name='b2_slider_2')
    position = models.IntegerField(verbose_name='Порядковый номер баннера')

    class Meta:
        verbose_name = 'Нижний Баннер типа №2'
        verbose_name_plural = 'Нижний Баннера типа №2'

    def __str__(self):
        return f"Нижний Баннер №2, порядковый номер - {self.position}"


class LowerBanner3(models.Model):
    """Нижний Баннер №3"""
    slider_1 = models.ManyToManyField('FotoForLowerBanner', verbose_name='Выбрать фото для слайдера', blank=True, related_name='b3_slider_1')
    link_block_1 = models.ManyToManyField(TextForLowerBanner, verbose_name='Блок ссылок №1', related_name='b3_link_1')
    slider_2 = models.ManyToManyField('FotoForLowerBanner', verbose_name='Выбрать фото для слайдера', blank=True, related_name='b3_slider_2')
    link_block_2 = models.ManyToManyField(TextForLowerBanner, verbose_name='Блок ссылок №2', related_name='b3_link_2')
    position = models.IntegerField(verbose_name='Порядковый номер баннера')

    class Meta:
        verbose_name = 'Нижний Баннер типа №3'
        verbose_name_plural = 'Нижний Баннера типа №3'

    def __str__(self):
        return f"Нижний Баннер №3, порядковый номер - {self.position}"


class AllLowerBanners(models.Model):
    """Модель списка всех нижних баннеров"""
    low_banner_1 = models.ForeignKey(LowerBanner1, on_delete=models.CASCADE, blank=True, null=True)
    low_banner_2 = models.ForeignKey(LowerBanner2, on_delete=models.CASCADE, blank=True, null=True)
    low_banner_3 = models.ForeignKey(LowerBanner3, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Список всех баннеров'
        verbose_name_plural = 'Список всех баннеров'
        # ordering = ('low_banner_1', 'low_banner_2', 'low_banner_3',)


    def __str__(self):
        if self.low_banner_1 != None:
            return str(self.low_banner_1)
        elif self.low_banner_2 != None:
            return str(self.low_banner_2)
        elif self.low_banner_3 != None:
            return str(self.low_banner_3)
        else:
            return str(self.id)


class LowerBannerForMainPage(models.Model):
    """Нижний баннер для главной страницы"""
    selected_banners = SortedManyToManyField(AllLowerBanners)

    class Meta:
        verbose_name = 'Нижний баннер главной страницы'
        verbose_name_plural = 'Нижний баннер главной страницы'

    def __str__(self):
        return 'Нижний баннер главной страницы'

# Добавление баннера №1 в список всех баннеров
@receiver(post_save, sender=LowerBanner1)
def save_b1_to_all_banners(sender, instance, **kwargs):
    AllLowerBanners.objects.create(low_banner_1_id=instance.id)

# Удаление баннера №1 из списка всех баннеров
@receiver(pre_delete, sender=LowerBanner1)
def delete_b1_from_all_banners(sender, instance, **kwargs):
    banner = AllLowerBanners.objects.get(low_banner_1_id=instance.id)
    banner.delete()

# Добавление баннера №2 в список всех баннеров
@receiver(post_save, sender=LowerBanner2)
def save_b2_to_all_banners(sender, instance, **kwargs):
    AllLowerBanners.objects.create(low_banner_2_id=instance.id)

# Удаление баннера №2 из списка всех баннеров
@receiver(pre_delete, sender=LowerBanner2)
def delete_b2_from_all_banners(sender, instance, **kwargs):
    banner = AllLowerBanners.objects.get(low_banner_2_id=instance.id)
    banner.delete()

# Добавление баннера №3 в список всех баннеров
@receiver(post_save, sender=LowerBanner3)
def save_b3_to_all_banners(sender, instance, **kwargs):
    AllLowerBanners.objects.create(low_banner_3_id=instance.id)

# Удаление баннера №3 из списка всех баннеров
@receiver(pre_delete, sender=LowerBanner3)
def delete_b3_from_all_banners(sender, instance, **kwargs):
    banner = AllLowerBanners.objects.get(low_banner_3_id=instance.id)
    banner.delete()
