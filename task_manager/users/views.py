from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from task_manager.users.forms import RegisterUserForm, UsersChangeForm
from task_manager.users.models import User
from task_manager.utils import (MixinDeleteUser, MixinLoginRequired,
                                MixinUpdateUser)


def users(request):
    user = User.objects.all()
    return render(request, 'users/users.html', context={'user': user})


class UsersCreate(SuccessMessageMixin,
                  CreateView):
    form_class = RegisterUserForm
    model = User
    template_name = 'actions/create_or_update.html'
    success_message = ('Пользователь успешно зарегистрирован')
    success_url = reverse_lazy('login')
    extra_context = {
        'title': 'Регистрация',
        'button_text': 'Зарегистрировать',
    }


class UsersUpdate(MixinLoginRequired,
                  SuccessMessageMixin,
                  MixinUpdateUser):
    form_class = UsersChangeForm
    model = User
    template_name = 'actions/create_or_update.html'
    success_url = reverse_lazy('users')
    pk_url_kwarg = 'user_id'
    success_message = ('Пользователь успешно изменен')
    extra_context = {
        'title': 'Изменение пользователя',
        'button_text': 'Изменить',
    }
    messages_for_error = 'У вас нет прав для изменения другого пользователя.'
    redirect_for_error = 'users'


class UserDelete(MixinLoginRequired,
                 SuccessMessageMixin,
                 MixinDeleteUser):
    model = User
    template_name = 'actions/delete.html'
    success_url = reverse_lazy('users')
    pk_url_kwarg = 'user_id'
    success_message = ('Пользователь успешно удален')
    extra_context = {
        'title': 'Удаление пользователя',
        'button_text': 'Удалить',
    }
    messages_for_error_get = '''Невозможно удалить пользователя,
    потому что он используется'''
    messages_for_error_post = '''У вас нет прав для
    изменения другого пользователя.'''
    redirect_for_error = 'users'
