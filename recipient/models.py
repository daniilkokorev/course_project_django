from django.db import models

from users.models import User

NULLABLE = {"blank": True, "null": True}


class Recipient(models.Model):
    email = models.EmailField(max_length=100, unique=True, verbose_name='Почта')
    name = models.CharField(max_length=100, verbose_name='Имя')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE, verbose_name='Владелец')

    class Meta:
        verbose_name = 'Получатель'
        verbose_name_plural = 'Получатели'

    def __str__(self):
        return self.email
