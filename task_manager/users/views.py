from django.shortcuts import render, redirect
from task_manager.users.models import Users
from task_manager.users.forms import RegisterUserForm, UsersChangeForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth import get_user_model
from django.contrib.messages.views import SuccessMessageMixin


def users(request):
    user = Users.objects.all()
    return render(request, 'users/users.html', context={'user': user})


class UsersCreate(SuccessMessageMixin, CreateView):
    form_class = RegisterUserForm
    model = Users
    template_name = 'actions/create_or_update.html'
    success_url = reverse_lazy('login')
    extra_context = {
        'title': 'Регистрация',
        'button_text': 'Удалить',
    }


class UsersUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = UsersChangeForm
    model = Users
    template_name = 'actions/create_or_update.html'
    success_url = reverse_lazy('login')
    pk_url_kwarg = 'user_id'
    extra_context = {
        'title': 'Изменение пользователя',
        'button_text': 'Удалить',
    }
    

class UserDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Users
    template_name = 'actions/delete.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'user_id'
    extra_context = {
        'title': 'Удаление пользователя',
        'button_text': 'Удалить',
    }

