from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django_filters.views import FilterView

from task_manager.utils import FilterTasks, MixinDeleteTask, MixinLoginRequired

from .forms import CreateUpdateTaskForm
from .models import Tasks


class TaskHome(MixinLoginRequired,
               SuccessMessageMixin,
               FilterView,
               ListView):
    template_name = 'tasks/tasks.html'
    context_object_name = 'tasks1'
    filterset_class = FilterTasks
    allow_empty = False
    extra_context = {
        'title': 'Задачи',
        'button_text': 'Показать',
    }

    def get_queryset(self):
        return Tasks.objects.all()


class TaskCreate(MixinLoginRequired,
                 SuccessMessageMixin,
                 CreateView):
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


class Task(MixinLoginRequired,
           SuccessMessageMixin,
           DetailView):
    model = Tasks
    template_name = 'tasks/task.html'
    fields = ['task_name', 'description', 'status', 'executor', 'labels']
    context_object_name = 'task'
    pk_url_kwarg = 'task_id'
    extra_context = {
        'title': 'Просмотр задачи',
    }


class TaskUpdate(MixinLoginRequired,
                 SuccessMessageMixin,
                 UpdateView):
    form_class = CreateUpdateTaskForm
    model = Tasks
    template_name = 'actions/create_or_update.html'
    success_url = reverse_lazy('tasks')
    pk_url_kwarg = 'task_id'
    success_message = ('Задача успешно изменена')
    extra_context = {
        'title': 'Изменение задачи',
        'button_text': 'Изменить',
    }


class TaskDelete(MixinLoginRequired,
                 SuccessMessageMixin,
                 MixinDeleteTask):
    model = Tasks
    template_name = 'actions/delete.html'
    success_url = reverse_lazy('tasks')
    pk_url_kwarg = 'task_id'
    success_message = ('Задача успешно удалена')
    extra_context = {
        'title': 'Удаление задачи'
    }
    messages_for_error = 'Задачу может удалить только ее автор'
    redirect_for_error = 'tasks'
