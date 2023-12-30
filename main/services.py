from datetime import datetime

from django.core.cache import cache
from django.core.mail import send_mail

from blog.models import Blog
from config import settings
# from config.settings import CACHE_ENABLED
from main.models import Newsletter, NewsletterLog


def send_order_email(obj: Newsletter):
    try:
        send_mail(
            subject=obj.title_message,
            message=obj.body_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[*obj.client.all()],
            fail_silently=True)
        logs = NewsletterLog.objects.create( 
            mailing=obj,
            datetime_of_last_attempt=datetime.now(),
            status=True,
            error_msg='200 OK'
        )
    except Exception as e:
        logs = NewsletterLog.objects.create(
            mailing=obj,
            datetime_of_last_attempt=datetime.now(),
            status=False,
            error_msg=str(e)
        )


def time_task():
    current_date = datetime.now().date()
    mailings_created = Newsletter.objects.filter(status='created')

    if mailings_created.exists():
        for mailing in mailings_created:
            if mailing.start_time <= current_date <= mailing.end_time:
                mailing.status = 'started'
                mailing.save()

    mailings_launched = Newsletter.objects.filter(status='started')

    if mailings_launched.exists():
        for mailing in mailings_launched:
            if mailing.start_time <= current_date <= mailing.end_time:
                if mailing.last_run:
                    differance = current_date - mailing.last_run
                    if mailing.period == 'daily':
                        if differance.days == 1:
                            send_order_email(mailing)
                            mailing.last_run = current_date
                            mailing.save()
                    elif mailing.period == 'weekly':
                        if differance.days == 7:
                            send_order_email(mailing)
                            mailing.last_run = current_date
                            mailing.save()
                    elif mailing.period == 'monthly':
                        if differance.days == 30:
                            send_order_email(mailing)
                            mailing.last_run = current_date
                            mailing.save()
                else:
                    send_order_email(mailing)
                    mailing.last_run = current_date
                    mailing.save()

            elif current_date >= mailing.end_time:
                mailing.status = 'done'
                mailing.save()


# def cache_blog():
#     if CACHE_ENABLED:
#         # Проверяем включенность кеша
#         key = f'blog_list'  # Создаем ключ для хранения
#         blog_list = cache.get(key)  # Пытаемся получить данные
#         if blog_list is None:
#             # Если данные не были получены из кеша, то выбираем из БД и записываем в кеш
#             blog_list = Blog.objects.all()
#             cache.set(key, blog_list)
#     else:
#         # Если кеш не был подключен, то просто обращаемся к БД
#         blog_list = Blog.objects.all()
#     # Возвращаем результат
#     return blog_list