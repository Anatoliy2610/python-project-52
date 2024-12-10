from django.shortcuts import render
from task_manager.users.models import Users
from task_manager.users.forms import RegisterUserForm, UsersChangeForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin

from task_manager.utils import MixinDeleteUser, MixinUpdateUser


def users(request):
    user = Users.objects.all()
    return render(request, 'users/users.html', context={'user': user})


class UsersCreate(SuccessMessageMixin, CreateView):
    form_class = RegisterUserForm
    model = Users
    template_name = 'actions/create_or_update.html'
    success_message = ('Пользователь успешно создан')
    success_url = reverse_lazy('login')
    extra_context = {
        'title': 'Регистрация',
        'button_text': 'Создать',
    }


class UsersUpdate(LoginRequiredMixin, SuccessMessageMixin, MixinUpdateUser):
    form_class = UsersChangeForm
    model = Users
    template_name = 'actions/create_or_update.html'
    success_url = reverse_lazy('users:home')
    pk_url_kwarg = 'user_id'
    success_message = ('Пользователь успешно изменен')
    extra_context = {
        'title': 'Изменение пользователя',
        'button_text': 'Изменить',
    }
    messages_for_error = 'У вас нет прав для изменения другого пользователя.'
    redirect_for_error = 'users:home'


class UserDelete(LoginRequiredMixin, SuccessMessageMixin, MixinDeleteUser):
    model = Users
    template_name = 'actions/delete.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'user_id'
    success_message = ('Пользователь успешно удален')
    extra_context = {
        'title': 'Удаление пользователя',
        'button_text': 'Удалить',
    }
    messages_for_error_get = 'Невозможно удалить пользователя, потому что он используется'
    messages_for_error_post = 'У вас нет прав для изменения другого пользователя.'
    redirect_for_error = 'home'


