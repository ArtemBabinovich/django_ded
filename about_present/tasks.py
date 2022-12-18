import datetime

from celery import shared_task
from dateutil.relativedelta import relativedelta
from django.core.mail import EmailMultiAlternatives, send_mail
from django.db.models import Prefetch

from about_present.models import AboutPresent, Date
from ded import settings
from ded.celery import app
from .telegram import bot, chat_id


# отправка подтверждения на эмейл о заказе
# TODO поправить try: except: Доделать шаблон письма
@app.task
def send(user_email):
    try:
        # message = Message.objects.first().text
        message = 'some_text'
        subject_message = 'some_text'
        # subject_message = SubjectMessage.objects.first().text
    except:
        message = 'Ваш заказ принят. Ожидайте, с вами свяжутся. Благодарю за заказ'
        subject_message = 'Заказ'

    subject, from_email, to = subject_message, settings.DEFAULT_USER_MAIL, [user_email]
    text_content = ''
    html_content = message
    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, "text/html")
    msg.send()


# отправка периодических уведолений каждый год
# TODO нужен шаблон письма
@app.task
def send_periodic_email_every_year():
    query_dates = AboutPresent.objects.filter(remind_every_years=True) \
        .prefetch_related(Prefetch('about_present', queryset=Date.objects.all()))
    for i in query_dates:
        for j in i.about_present.all():
            if datetime.date.today() == (j.date - datetime.timedelta(days=i.remind_for_days.days)):
                send_mail(
                    'какой-то текст',
                    'текстовое сообщение',
                    settings.DEFAULT_USER_MAIL,
                    [i.email],
                    fail_silently=False
                )
                new_date = j.date + relativedelta(years=+1)
                update_date = i.about_present.get(id=j.id)
                update_date.date = new_date
                update_date.save()


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
