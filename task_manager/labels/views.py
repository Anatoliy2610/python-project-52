from django.shortcuts import render, get_object_or_404, redirect
from .models import Labels
from .forms import CreateUpdateLabelForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin


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
        'title': 'Изменение метк',
        'button_text': 'Изменить',
    }


class LabelsDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Labels
    template_name = 'actions/delete.html'
    success_url = reverse_lazy('labels')
    pk_url_kwarg = 'label_id'
    extra_context = {
        'title': 'Удаление метки',
        'button_text': 'Удалить',
    }



