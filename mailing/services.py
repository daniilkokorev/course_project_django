from django.core.cache import cache
from blog.models import Blog
from config.settings import CACHE_ENABLED
import smtplib
import pytz
from datetime import datetime, timedelta
from django.core.mail import send_mail
from config import settings
from mailing.models import MailingSettings, MailingStatus
from dateutil.relativedelta import relativedelta


def get_blog_from_cache():
    """
    Функция для получения блога из кэша
    """
    if not CACHE_ENABLED:
        return Blog.objects.filter(is_published=True)[:3]
    key = 'blog_list'
    blog = cache.get(key)
    if blog is not None:
        return blog
    blog = Blog.objects.filter(is_published=True)[:3]
    cache.set(key, blog)
    return blog


def send_email():
    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)

    mailings = MailingSettings.objects.filter(first_datetime__lte=current_datetime).filter(
        status__in=['Create', 'Started'])

    for mailing in mailings:
        if mailing.first_datetime is None:
            mailing.first_datetime = current_datetime
        title = mailing.message.title
        content = mailing.message.content
        mailing.status = 'Started'
        mailing.save()
        try:
            if mailing.last_datetime < mailing.first_datetime:
                mailing.first_datetime = current_datetime
                mailing.status = 'Done'
                mailing.save()
                continue
            if mailing.first_datetime <= current_datetime:
                server_response = send_mail(
                    subject=title,
                    message=content,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[recipient.email for recipient in mailing.recipient.all()],
                    fail_silently=False,
                )
                if server_response == 1:
                    server_response = 'Письмо успешно отправлено'
                MailingStatus.objects.create(status='success', mailing_response=server_response, mailing_list=mailing)

                if mailing.frequency == 'daily':
                    mailing.first_datetime = current_datetime + timedelta(days=1)

                elif mailing.frequency == 'weekly':
                    mailing.first_datetime = current_datetime + timedelta(days=7)

                elif mailing.frequency == 'monthly':
                    mailing.first_datetime = current_datetime + relativedelta(months=1)

            mailing.save()

        except smtplib.SMTPException as error:
            MailingStatus.objects.create(status='fail', mailing_response=error, mailing_list=mailing)
