from django.contrib.auth import get_user_model
from django.db import models

from task_manager.labels.models import Labels
from task_manager.statuses.models import Statuses
from task_manager.users.models import User


class Tasks(models.Model):
    task_name = models.CharField(
        max_length=255,
        verbose_name='Имя')
    time_create = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания')
    description = models.TextField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Описание')
    status = models.ForeignKey(
        Statuses,
        on_delete=models.PROTECT,
        null=True,
        verbose_name='Статус',
        related_name='status')
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        null=True,
        related_name='author')
    executor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=True,
        verbose_name='Исполнитель',
        related_name='executor')
    labels = models.ManyToManyField(
        Labels,
        blank=True,
        verbose_name='Метки',
        related_name='labels')

    def __str__(self):
        return self.task_name
