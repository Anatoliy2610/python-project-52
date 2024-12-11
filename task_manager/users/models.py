from django.contrib.auth.models import AbstractUser
from django.db import models


class Users(AbstractUser):
    time_create = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания')

    def __str__(self):
        return self.get_full_name()
