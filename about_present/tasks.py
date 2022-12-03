from celery import shared_task

from .models import AboutPresent
from .telegram import bot, chat_id


# Отправка сообщения в чат бот при оформлении заявки на подарок
@shared_task
def send_to_telegram(obj_id, chat_id=chat_id):
    response = AboutPresent.objects.get(id=obj_id)
    dates = ''
    if response.remind_every_day == True:
        remind_every_day = 'Да'
    else:
        remind_every_day = 'Нет'
    if response.remind_every_years == True:
        remind_every_years = 'Да'
    else:
        remind_every_years = 'Нет'
    for i in response.dates.all():
        dates += f'{i}\n'
    telegram_message = f'Получена заявка на получения подарка \n' \
                       f'Имя пользователя: {response.name} \n' \
                       f'email: {response.email} \n' \
                       f'{f"Телефон: {response.phone}" if response.phone else "Телефон: не указан"} \n' \
                       f'Заявленные даты: {dates}' \
                       f'Получатель: {response.recipient}\n' \
                       f'Повод: {response.reason} \n' \
                       f'Вид подарка: {response.present}\n' \
                       f'Напомнить о подарке за: {response.remind_for_days} дней\n' \
                       f'Напоминание каждый день: {remind_every_day}\n' \
                       f'Напоминание каждый год: {remind_every_years}\n' \
                       f'Дата оформления заявки: {response.date_created}\n'
    bot.sendMessage(chat_id=chat_id, text=telegram_message)
