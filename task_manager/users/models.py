from django.db import models
from django.contrib.auth.models import AbstractUser


'''
команды для миграций
python3 manage.py makemigrations
python3 manage.py migrate
'''


class Users(AbstractUser):
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.get_full_name()
