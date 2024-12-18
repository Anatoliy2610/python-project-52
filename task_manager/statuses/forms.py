from django import forms

from .models import Statuses


class CreateUpdateStatusForm(forms.ModelForm):
    class Meta:
        model = Statuses
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(
                attrs={"placeholder": "Имя", "class": "form-control"}
            )
        }

    def clean_status_name(self):
        name = self.cleaned_data["name"]
        if Statuses.objects.filter(name=name):
            raise forms.ValidationError("Task status с таким Имя уже существует.")
        return name
