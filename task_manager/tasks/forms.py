from django import forms
from .models import Tasks


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
    
    def clean_task_name(self):
        task_name = self.cleaned_data['task_name']
        if Tasks.objects.filter(task_name=task_name):
            raise forms.ValidationError('Task с таким Имя уже существует.')
        return task_name 