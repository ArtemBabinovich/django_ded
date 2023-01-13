from django.db import models
from django.core.exceptions import ValidationError


class SubscribeSocialNetworksModel(models.Model):
    """Модель для формирования общего блока соц. сетей"""
    title = models.CharField("Название блока", max_length=255)
    title2 = models.CharField("Дополнительное название", max_length=255, blank=True, null=True)
    social_networks = models.ManyToManyField('AddSocialNetworks',
                                        blank=True,
                                        verbose_name='Какие социальные сети добавить',
                                        related_name='networks')

    class Meta:
        verbose_name = 'Блок социальных сетей'
        verbose_name_plural = 'Блок социальных сетей'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.pk and SubscribeSocialNetworksModel.objects.exists():
            raise ValidationError('Можно создать только одну запись а базе')
        return super(SubscribeSocialNetworksModel, self).save(*args, **kwargs)



class AddSocialNetworks(models.Model):
    """Модель для создания ссылок на социальную сеть"""
    url_social_network = models.CharField('Ссылка на социальную сеть', max_length=511)
    image = models.ImageField('Добавить фотографию', upload_to='social_networks/static/img')

    class Meta:
        verbose_name = 'Создать ссылку на социальную сеть'
        verbose_name_plural = 'Создать ссылку на социальную сеть'

    def __str__(self):
        return f"Соц.сеть {self.url_social_network}"


