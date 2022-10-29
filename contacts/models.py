from django.db import models


class SocialNetworks(models.Model):
    """Социальные сети"""
    logo = models.ImageField('Логотип социальной сети', upload_to='social_networks/image/')
    name = models.CharField('Название социальной сети', max_length=50)
    link = models.URLField('Ссылка на социальную сеть', max_length=255)

    class Meta:
        verbose_name = 'Социальная сети'
        verbose_name_plural = 'Социальные сети'

    def __str__(self):
        return self.name
