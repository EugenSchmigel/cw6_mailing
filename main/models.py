from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Customer(models.Model):
    fio = models.CharField(max_length=100, verbose_name='ФИО')
    email = models.EmailField(verbose_name='контактный email')
    comment = models.TextField(**NULLABLE, verbose_name='комментарий')
    create_date = models.DateTimeField(**NULLABLE, verbose_name='дата создания')

    def __str__(self):
        return f'{self.fio}, ({self.email})'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Message(models.Model):
    message_subject = models.CharField(max_length=100, verbose_name='тема письма')
    message_body = models.TextField(verbose_name='тело письма', **NULLABLE)
    create_date = models.DateTimeField(**NULLABLE, verbose_name='дата создания')

    def __str__(self):
        return f'{self.message_subject}'

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщений'


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
    message = models.ManyToManyField(Message, verbose_name='сообщение')
    create_date = models.DateTimeField(**NULLABLE, verbose_name='время рассылки')
    interval = models.CharField(max_length=20, choices=INTERVAL_CHOICES, **NULLABLE, verbose_name='периодичность')
    status = models.CharField(max_length=20, choices=STATUS, verbose_name='статус рассылки')

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
    create_date = models.DateTimeField(**NULLABLE, verbose_name='дата создания')

    def __str__(self):
        return f'{self.newsletter}, {self.mail_server_response}, {self.status}'

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'

