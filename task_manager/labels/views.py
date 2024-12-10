from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Labels
from .forms import CreateUpdateLabelForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import DeletionMixin
from django.db.models import ProtectedError
from django.contrib import messages
from task_manager.utils import MixinDeleteLabel


class LabelsHome(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = Labels
    template_name = 'labels/labels.html'
    context_object_name = 'labels'
    extra_context = {
        'title': 'Метки'
    }

    def get_queryset(self):
        return Labels.objects.all()


class LabelsCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = CreateUpdateLabelForm
    model = Labels
    template_name = 'actions/create_or_update.html'
    success_url = reverse_lazy('labels')
    success_message = ('Метка успешно создана')
    extra_context = {
        'title': 'Создать метку',
        'button_text': 'Создать',
    }


class LabelsUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = CreateUpdateLabelForm
    model = Labels
    template_name = 'actions/create_or_update.html'
    success_url = reverse_lazy('labels')
    pk_url_kwarg = 'label_id'
    extra_context = {
        'title': 'Изменение метки',
        'button_text': 'Изменить',
    }
    success_message = ('Метка успешно изменена')



class LabelsDelete(LoginRequiredMixin, SuccessMessageMixin,  MixinDeleteLabel):
    model = Labels
    template_name = 'actions/delete.html'
    pk_url_kwarg = 'label_id'
    context_object_name = 'labels1'
    extra_context = {
        'title': 'Удаление метки',
        'button_text': 'Удалить',
    }
    success_url = reverse_lazy('labels')
    success_message = ('Метка успешно удалена')
    messages_for_error = 'Невозможно удалить метку, потому что он используется'
    redirect_for_error = 'labels'



