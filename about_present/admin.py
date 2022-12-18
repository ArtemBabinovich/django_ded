from django.contrib import admin

from about_present.models import Reason, Present, RemindForDays, Recipient, AboutPresent


@admin.register(AboutPresent)
class AboutPresentAdmin(admin.ModelAdmin):
    """Модель просмотра кто заказал подарок"""
    fields = ('name', 'email', 'phone', 'recipient', 'reason', 'present', 'remind_for_days', 'remind_every_years')
    list_display = ('name', 'email', 'phone', 'recipient', 'reason', 'present', 'remind_for_days', 'remind_every_years')


@admin.register(Reason)
class ReasonAdmin(admin.ModelAdmin):
    """Модель Повод для подарка"""

    fields = ('name',)


@admin.register(Present)
class PresentAdmin(admin.ModelAdmin):
    """Модель Тип подарка"""

    fields = ('name',)


@admin.register(RemindForDays)
class RemindForDaysAdmin(admin.ModelAdmin):
    """Модель За какое количество дней напомнить"""

    fields = ('days',)


@admin.register(Recipient)
class RecipientAdmin(admin.ModelAdmin):
    """Модель Для кого подарок"""

    fields = ('name',)
