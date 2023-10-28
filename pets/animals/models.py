from django.db import models


# Create your models here.
class Animal(models.Model):
    title = models.CharField(
        'Имя',
        max_length=300,)
    description = models.TextField(
        'Описание',
        blank=True)
    time_create = models.DateTimeField(
        'Время создания записи',
        auto_now_add=True)
    time_update = models.DateTimeField(
        'Время изменения записи',
        auto_now=True)
    is_published = models.BooleanField(
        'Опубликована запись или нет',
        default=True)
    category = models.ForeignKey(
        'Category',
        on_delete=models.PROTECT,
        null=True
    )

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(
        'Название категории',
        max_length=100,
        db_index=True)

    def __str__(self):
        return self.name
