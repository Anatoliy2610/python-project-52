from typing import Any
from django.core.handlers.wsgi import WSGIRequest
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from task_manager.users.forms import LoginUserForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, TemplateView
from task_manager.users.models import Users
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


class LoginUser(SuccessMessageMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'
    success_message = 'Вы залогинены'
    extra_context = {
        'title': 'Вход',
        'button_text': 'Войти'
        }

    def get_success_url(self) -> str:
        return reverse_lazy('home')

class LogoutUser(LogoutView):
    next_page = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, "Вы разлогинены")
        return super().dispatch(request, *args, **kwargs)


