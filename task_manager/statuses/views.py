from django.shortcuts import render, get_object_or_404, redirect
from .models import Statuses
from .forms import CreateUpdateStatusForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from task_manager.utils import MixinDeleteStatus


class StatusesHome(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = Statuses
    template_name = 'statuses/statuses.html'
    context_object_name = 'statuses'
    extra_context = {
        'title': 'Статусы'
    }

    def get_queryset(self):
        return Statuses.objects.all()
    

class StatusesCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = CreateUpdateStatusForm
    model = Statuses
    template_name = 'actions/create_or_update.html'
    success_url = reverse_lazy('statuses')
    success_message = ('Статус успешно создан')
    extra_context = {
        'title': 'Создать статус',
        'button_text': 'Создать',
    }


class StatusesUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = CreateUpdateStatusForm
    model = Statuses
    template_name = 'actions/create_or_update.html'
    success_url = reverse_lazy('statuses')
    success_message = ('Статус успешно изменен')
    pk_url_kwarg = 'status_id'
    extra_context = {
        'title': 'Изменение статуса',
        'button_text': 'Изменить',
    }


class StatusesDelete(LoginRequiredMixin, SuccessMessageMixin, MixinDeleteStatus):
    model = Statuses
    template_name = 'actions/delete.html'
    success_url = reverse_lazy('statuses')
    success_message = ('Статус успешно удален')
    pk_url_kwarg = 'status_id'
    extra_context = {
        'title': 'Удаление статуса'
    }
    messages_for_error = 'Невозможно удалить статус, потому что он используется'
    redirect_for_error = 'statuses'
