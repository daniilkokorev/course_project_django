from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    """
    Класс для моделей пользователей
    """
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')

    avatar = models.ImageField(upload_to="users/media", **NULLABLE, verbose_name="Аватар")
    phone = models.CharField(max_length=35, verbose_name='Телефон')
    country = models.CharField(max_length=50, verbose_name='Страна')

    token = models.CharField(max_length=80, verbose_name='token', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
