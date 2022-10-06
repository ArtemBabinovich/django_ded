from django.db import models


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
