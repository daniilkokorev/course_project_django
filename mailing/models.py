from django.db import models

NULLABLE = {"blank": True, "null": True}
FREQUENCY_CHOICES = [('daily', 'раз в день'), ('weekly', 'раз в неделю'), ('monthly', 'раз в месяц'), ]
STATUS_OF_NEWSLETTER = [('Create', 'Создана'), ('Started', 'Отправлено'), ('Done', 'Завершена'), ]


class Message(models.Model):
    """
    Модель сообщения
    """
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Контент')

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return self.title
