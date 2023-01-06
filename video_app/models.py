from django.db import models


class Video(models.Model):
    """Модель для добавления ссылок на видео"""
    url = models.CharField('Ссылка на видео', max_length=512)
    description = models.CharField('Описание видео', max_length=255)
    description2 = models.CharField('Дополнительное описание', max_length=128, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Добавить ссылку на видео'
        verbose_name_plural = 'Добавить ссылку на видео'

    def __str__(self):
        return 'Ссылка на видео'
