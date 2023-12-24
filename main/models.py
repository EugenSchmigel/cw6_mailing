from django.contrib.auth.models import User
from django.db import models
# from users.models import User


NULLABLE = {'blank': True, 'null': True}


class Customer(models.Model):
    fio = models.CharField(max_length=100, verbose_name='ФИО')
    email = models.EmailField(verbose_name='контактный email')
    comment = models.TextField(**NULLABLE, verbose_name='комментарий')
    create_date = models.DateTimeField(**NULLABLE, auto_now_add=True, verbose_name='дата создания')
    # owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='владелец', **NULLABLE)


    def __str__(self):
        return f'{self.fio}, ({self.email})'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Newsletter(models.Model):

    STATUS = [
        ('started', 'Запущена'),
        ('created', 'Создана'),
        ('completed', 'Завершена')
    ]

    INTERVAL_CHOICES = [
        ('daily', 'раз в день'),
        ('weekly', 'раз в день'),
        ('monthly', 'раз в месяц'),
    ]

    customer = models.ManyToManyField(Customer, verbose_name='клиент')
    create_date = models.DateTimeField(**NULLABLE, auto_now_add=True, verbose_name='время рассылки')
    interval = models.CharField(max_length=20, choices=INTERVAL_CHOICES, **NULLABLE, verbose_name='периодичность')
    status = models.CharField(max_length=20, choices=STATUS, verbose_name='статус рассылки')
    message_subject = models.CharField(max_length=100, verbose_name='тема письма')
    message_body = models.TextField(verbose_name='тело письма', **NULLABLE)
    # owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='владелец', **NULLABLE)
    start_time = models.DateField(**NULLABLE, verbose_name='начало рассылки')
    end_time = models.DateField(**NULLABLE, verbose_name='конец рассылки')
    last_run = models.DateField(verbose_name='дата последней отправки рассылки', **NULLABLE)

    def __str__(self):
        return f'{self.create_date} - {self.interval} ({self.status}  - {self.customer}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'



class NewsletterLog(models.Model):

    STATUS = [
        ('successful', 'Успешно'),
        ('failed', 'Запущена')
    ]

    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE, **NULLABLE, verbose_name='рассылка')
    status = models.CharField(max_length=50, choices=STATUS, verbose_name='статус попытки')
    mail_server_response = models.TextField(**NULLABLE, verbose_name='ответ почтового сервера')
    create_date = models.DateTimeField(**NULLABLE, auto_now_add=True, verbose_name='дата создания')
    datetime_of_last_attempt = models.DateTimeField(verbose_name='дата и время последней попытки')

    def __str__(self):
        return f'{self.newsletter}, {self.mail_server_response}, {self.status}'

    class Meta:
        verbose_name = 'Лог рассылки'
        verbose_name_plural = 'Логи рассылки'