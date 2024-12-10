from typing import Any
from django.db import models
from django.urls import reverse


class Labels(models.Model):
    label_name = models.CharField(max_length=255, verbose_name='Имя')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.label_name
