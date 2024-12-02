from django import forms
from .models import Tasks
from task_manager.statuses.models import Statuses


class CreateUpdateTaskForm(forms.ModelForm):

    class Meta:
        model = Tasks
        fields = [
            'task_name',
            'description',
            'status',
            'executor',
            'labels',
            ]
        widgets = {
            'task_name': forms.TextInput(attrs={'class': 'form-input'}),
            'task_name': forms.TextInput(attrs={'class': 'form-label'}),
            'task_name': forms.TextInput(attrs={'class': 'mb-3'})}
