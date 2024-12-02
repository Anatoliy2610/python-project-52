from django_filters import FilterSet, ModelChoiceFilter, BooleanFilter
from task_manager.statuses.models import Statuses
from task_manager.tasks.models import Tasks
from task_manager.labels.models import Labels
from task_manager.users.models import Users
from django.forms import CheckboxInput



'''
1. url tasks - поправить форму
2. удаление пользователей - самими пользователями; изменение - могут только сами пользователи
3. удаление статуса если он используется ; изменение - могут все
4. удаление меток если они используются; изменение - могут все
5. удаление задач только теми, кто сделал; изменение - могут все
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


