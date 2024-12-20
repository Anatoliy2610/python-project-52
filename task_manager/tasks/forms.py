from django import forms
from django.utils.translation import gettext as _

from .models import Tasks


class CreateUpdateTaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = [
            "name",
            "description",
            "status",
            "executor",
            "labels",
        ]

    def clean_task_name(self):
        name = self.cleaned_data["name"]
        if Tasks.objects.filter(name=name):
            raise forms.ValidationError(
                _("A Task with this Name already exists.")
            )
        return name
