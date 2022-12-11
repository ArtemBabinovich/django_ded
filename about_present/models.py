from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models

from modules.models import validate_current_century


"""Функция для дефолтного значения календаря"""
def get_default_name():
    try:
        about_present, created = OnlyGetAboutPresent.objects.get_or_create(name='calendar_dates')
        return about_present
    except:
        return None


class OnlyGetAboutPresent(models.Model):
    """Модель для АРI view напоминание о подарке"""
    name = models.CharField(default='calendar_dates', null=True, blank=True, max_length=30)

    def save(self, *args, **kwargs):
        if not self.pk and OnlyGetAboutPresent.objects.exists():
            raise ValidationError('Можно создать только одну запись а базе')
        return super(OnlyGetAboutPresent, self).save(*args, **kwargs)

    def __str__(self):
        return "Заполнить календарь"

    class Meta:
        verbose_name = "API календаря"
        verbose_name_plural = "API календаря"


class Recipient(models.Model):
    """Для кого подарок"""
    name = models.CharField('Кому', max_length=50)
    about_preset = models.ForeignKey(OnlyGetAboutPresent, on_delete=models.SET_DEFAULT, default=get_default_name,
                                     null=True, blank=True, verbose_name='Календарь напоминаний')

    class Meta:
        verbose_name = 'Кому'
        verbose_name_plural = 'Кому'

    def __str__(self):
        return self.name


class Reason(models.Model):
    """Повод подарка"""
    name = models.CharField('Повод', max_length=50)
    about_preset = models.ForeignKey(OnlyGetAboutPresent, on_delete=models.SET_DEFAULT, default=get_default_name,
                                     null=True, blank=True, verbose_name='Календарь напоминаний')

    class Meta:
        verbose_name = 'Повод'
        verbose_name_plural = 'Повод'

    def __str__(self):
        return self.name


class Present(models.Model):
    """Тип подарка"""
    name = models.CharField('Что хотят заказать', max_length=50)
    about_preset = models.ForeignKey(OnlyGetAboutPresent, on_delete=models.SET_DEFAULT, default=get_default_name,
                                     null=True, verbose_name='Календарь напоминаний', blank=True)

    class Meta:
        verbose_name = 'Что хотят заказать'
        verbose_name_plural = 'Что хотят заказать'

    def __str__(self):
        return self.name


class Date(models.Model):
    """Дата события для вручения подарка"""
    date = models.DateField(validators=[validate_current_century], verbose_name='Дата события')
    presents = models.ForeignKey('AboutPresent',
                                 verbose_name='Какой подарок',
                                 on_delete=models.CASCADE,
                                 related_name='about_present')

    class Meta:
        verbose_name = 'Дата напоминания'
        verbose_name_plural = 'Дата напоминания'

    def __str__(self):
        return str(self.date)


class RemindForDays(models.Model):
    """За какое кол-во дней напомнить"""
    days = models.IntegerField(verbose_name='За сколько дней напоминать')
    about_preset = models.ForeignKey(OnlyGetAboutPresent, on_delete=models.SET_DEFAULT, default=get_default_name,
                                     null=True, blank=True, verbose_name='Календарь напоминаний')

    class Meta:
        verbose_name = 'За сколько дней напоминать'
        verbose_name_plural = 'За сколько дней напоминать'

    def __str__(self):
        return str(self.days)


class AboutPresent(models.Model):
    """Кто заказал напоминане для вручения подарка"""
    name = models.CharField('Имя заказчика', max_length=50)
    email = models.EmailField('Почта заказчика')
    phone = models.CharField('Телефон заказчика', max_length=18, blank=True, null=True,
                             validators=[RegexValidator(regex=r'^[-0-9+() ]{11,18}$',
                                                        message='Поле должно состоять из цифр или знаков + () -')])
    recipient = models.ForeignKey(Recipient, on_delete=models.CASCADE, verbose_name='Кому')
    reason = models.ForeignKey(Reason, on_delete=models.CASCADE, verbose_name='Повод')
    present = models.ForeignKey(Present, on_delete=models.CASCADE, verbose_name='Подарок')
    remind_for_days = models.ForeignKey(RemindForDays, models.CASCADE, verbose_name='За сколько дней напомнить')
    remind_every_years = models.BooleanField(default=False, verbose_name='Напоминать ежегодно')
    date_created = models.DateField(auto_created=True, auto_now_add=True, verbose_name='Дата оформления')

    class Meta:
        verbose_name = 'Кто заказал напоминание о подарке'
        verbose_name_plural = 'Кто заказал напоминание о подарке'

    def __str__(self):
        return (f'{self.name} - {self.present.name}')
