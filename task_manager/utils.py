from typing import Any
from django.http import HttpRequest, HttpResponse
from django_filters import FilterSet, ModelChoiceFilter, BooleanFilter
from task_manager.statuses.models import Statuses
from task_manager.tasks.models import Tasks
from task_manager.labels.models import Labels
from task_manager.users.models import Users
from django.forms import CheckboxInput
from django.contrib import messages
from django.views.generic import UpdateView, DeleteView
from django.shortcuts import redirect


'''
1. флеш сообщение если не залогинен, + Вы залогинены
2. нужно выделить класс для переопределения методов гет, пост может быть ещё что-то (удалять, изменять)

5. удаление задач - нельзя переходить по tasks/task_id/delete - флеш сообщение


7. добавить флеш сообщения
7. прохождение шагов
'''


class FilterTasks(FilterSet):
    status = ModelChoiceFilter(queryset=Statuses.objects.all(), label='Статус')
    labels = ModelChoiceFilter(queryset=Labels.objects.all(), label='Метка')
    executor = ModelChoiceFilter(queryset=Users.objects.all(), label='Исполнитель')
    tasks_user = BooleanFilter(label='Только свои задачи', widget=CheckboxInput, method='filter_tasks_user')

    def filter_tasks_user(self, queryset, name, value):
        if value:
            user = self.request.user
            return queryset.filter(author=user)
        return queryset

    class Meta:
        model = Tasks
        fields = ['status', 'executor', 'labels', 'tasks_user']


class MixinDeleteStatus(DeleteView):
    messages_for_error = None
    redirect_for_error = None
        
    def post(self, request, *args, **kwargs):
        if self.get_object().status.exists():
            messages.error(self.request, (self.messages_for_error))
            return redirect(self.redirect_for_error)
        return super().post(request, *args, **kwargs)


class MixinDeleteLabel(DeleteView):
    messages_for_error = None
    redirect_for_error = None

    def post(self, request, *args, **kwargs):
        if self.get_object().labels.exists():
            messages.error(self.request, (self.messages_for_error))
            return redirect(self.redirect_for_error)
        return super().post(request, *args, **kwargs)


class MixinDeleteTask(DeleteView):
    messages_for_error = None
    redirect_for_error = None

    def get(self, request, *args, **kwargs):
        if self.get_object().author != self.request.user:
            messages.error(self.request, ('Задачу может удалить только ее автор'))
            return redirect(self.redirect_for_error)
        return super().get(request, *args, **kwargs)


class MixinDeleteUser(DeleteView):
    messages_for_error_get = None
    messages_for_error_post = None
    redirect_for_error = None

    def get(self, request, *args, **kwargs):
        if self.get_object().username != self.request.user.username:
            messages.error(self.request, (self.messages_for_error_get))
            return redirect(self.redirect_for_error)
        return super().get(request, *args, **kwargs)
        
    def post(self, request, *args, **kwargs):

        if Tasks.objects.filter(author=self.get_object().id):
            messages.error(self.request, (self.messages_for_error_post))
            return redirect(self.redirect_for_error)
        return super().post(request, *args, **kwargs)


class MixinUpdateUser(UpdateView):
    messages_for_error = None
    redirect_for_error = None

    def get(self, request, *args, **kwargs):
        if self.get_object().username != self.request.user.username:
            messages.error(self.request, (self.messages_for_error))
            return redirect(self.redirect_for_error)
        return super().get(request, *args, **kwargs)
