from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from task_manager.users.forms import LoginUserForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, TemplateView
from task_manager.users.models import Users
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy


from task_manager.tasks.models import Tasks
from django.views.generic import (ListView, CreateView, UpdateView,
                                  DeleteView, DetailView)


def index(request):
    return render(request, 'index.html')


# def login_user(request):
#     if request.method == 'POST':
#         form = LoginUserForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request, username=cd['username'], password=cd['password'])
#             if user and user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect(reverse('home'))
#     form = LoginUserForm()
#     return render(request, 'login.html', context={'form': form})

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_success_url(self) -> str:
        return reverse_lazy('home')


# def logout_user(request):
#     logout(request)
#     return HttpResponseRedirect(reverse('home'))

