from django.shortcuts import render, redirect
from .models import Tasks
from .forms import CreateUpdateTaskForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from task_manager.utils import FilterTasks
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.views import FilterView
from django.contrib.messages.views import SuccessMessageMixin


class TaskHome(LoginRequiredMixin, SuccessMessageMixin, FilterView, ListView):
    template_name = 'tasks/tasks.html'
    context_object_name = 'tasks1'
    filterset_class = FilterTasks
    allow_empty = False
    extra_context = {
        'title': 'Задачи'
    }

    def get_queryset(self):
        return Tasks.objects.all()
    

class TaskCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = CreateUpdateTaskForm
    model = Tasks
    template_name = 'actions/create_or_update.html'
    success_url = reverse_lazy('tasks')
    success_message = ('Задача успешно создана')
    extra_context = {
        'title': 'Создать задачу',
        'button_text': 'Создать',
    }

    def form_valid(self, form):
        w = form.save(commit=False)
        w.author = self.request.user
        return super().form_valid(form)


class Task(LoginRequiredMixin, SuccessMessageMixin, DetailView):
    model = Tasks
    template_name = 'tasks/task.html'
    fields = ['task_name', 'description', 'status', 'executor', 'labels']
    context_object_name = 'task'
    pk_url_kwarg = 'task_id'
    extra_context = {
        'title': 'Просмотр задачи',
    }

class TaskUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = CreateUpdateTaskForm
    model = Tasks
    template_name = 'actions/create_or_update.html'
    success_url = reverse_lazy('tasks')
    pk_url_kwarg = 'task_id'
    extra_context = {
        'title': 'Изменение задачи',
        'button_text': 'Изменить',
    }


class TaskDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Tasks
    template_name = 'actions/delete.html'
    success_url = reverse_lazy('tasks')
    pk_url_kwarg = 'task_id'
    extra_context = {
        'title': 'Удаление задачи'
    }
    context_object_name = 'task'
    # def form_valid(self, form):
    #     if self.get_object
    #     return super().form_valid(form)


