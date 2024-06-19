from django.db import models

from recipient.models import NULLABLE
from users.models import User


# Create your models here.
# Создавайте свои модели здесь.


class Blog(models.Model):
    """
    Класс для моделей блога
    """
    name = models.CharField(
        max_length=150,
        verbose_name="Заголовок"
    )
    content = models.TextField(verbose_name="Содержание")
    preview = models.ImageField(
        upload_to="media/blog",
        **NULLABLE,
        verbose_name="Изображение"
    )
    created_at = models.DateField(
        verbose_name="Дата создания",
        auto_now_add=True,
        **NULLABLE
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name="Опубликовано"
    )
    view_count = models.IntegerField(
        default=0,
        verbose_name="Количество просмотров"
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE, verbose_name='Владелец')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
