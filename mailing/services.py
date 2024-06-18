import smtplib
import pytz
from datetime import datetime, timedelta
from django.core.mail import send_mail
from config import settings
from mailing.models import MailingSettings, MailingStatus, STATUS_CHOICES


def send_email():
    """
    Функция отправки письма
    """
    # определяем текущее время
    zone = pytz.timezone(settings.TIME_ZONE)
    current_time = datetime.now(zone)
    # определяем время начала рассылки
    mailings = MailingSettings.objects.filter(first_datetime__lte=current_time).filter(status__in=['Create'])
    # задаём данные для отправки письма
    for mailing in mailings:
        title = mailing.message.title
        content = mailing.message.content
        mailing.status = 'Started'
        mailing.save()
        # отправляем письмо
        try:
            server_response = send_mail(
                subject=title,
                message=content,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[client.email for client in mailing.recipient.all()],
                fail_silently=False,
            )
            # определяем статус рассылки
            if server_response == 1:
                server_response = 'Сообщение отправлено'
                MailingStatus.objects.create(status=STATUS_CHOICES[0][1], mailing_response=server_response,
                                             mailing_list=mailing)

            mailing.status = 'Create'
            # определяеем время рассылки
            if mailing.frequency == 'daily' and server_response == 1:
                current_time = MailingSettings.objects.get(frequency='daily')
                mailing.first_datetime = current_time.first_datetime + timedelta(days=1)
                mailing.status = 'Create'

            elif mailing.frequency == 'weekly' and server_response == 1:
                current_time = MailingSettings.objects.get(frequency='weekly')
                mailing.first_datetime = current_time.first_datetime + timedelta(days=7)
                mailing.status = 'Create'

            elif mailing.frequency == 'monthly' and server_response == 1:
                current_time = MailingSettings.objects.get(frequency='monthly')
                mailing.first_datetime = current_time.first_datetime + timedelta(days=30)
                mailing.status = 'Create'

            mailing.save()

        except smtplib.SMTPException as error:
            MailingStatus.objects.create(status=STATUS_CHOICES[1][1], mailing_response=error,
                                         mailing_list=mailing)
            mailing.status = 'Create'
