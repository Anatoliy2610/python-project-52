from django import forms
from .models import Statuses


class CreateUpdateStatusForm(forms.ModelForm):

    class Meta:
        model = Statuses
        fields = ['status_name']
        widgets = {'name': forms.TextInput(
            attrs={'placeholder': 'Имя',
                   'class': 'form-control'})}

    def clean_status_name(self):
        status_name = self.cleaned_data['status_name']
        if Statuses.objects.filter(status_name=status_name):
            raise forms.ValidationError(
                'Task status с таким Имя уже существует.')
        return status_name
