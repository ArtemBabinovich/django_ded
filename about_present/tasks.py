import datetime

from dateutil.relativedelta import relativedelta
from django.core.mail import EmailMultiAlternatives, send_mail
from django.db.models import Prefetch

from about_present.modelTASKmessage import Message, SubjectMessage
from about_present.models import AboutPresent, Date
from ded import settings
from ded.celery import app


# отправка подтверждения на эмейл о заказе
# TODO поправить try: except: Доделать шаблон письма
@app.task
def send(user_email):
    try:
        message = Message.objects.first().text
        subject_message = SubjectMessage.objects.first().text
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
#TODO нужен шаблон письма
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
