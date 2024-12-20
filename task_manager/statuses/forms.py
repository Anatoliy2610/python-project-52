from django import forms
from django.utils.translation import gettext as _

from .models import Statuses


class CreateUpdateStatusForm(forms.ModelForm):
    class Meta:
        model = Statuses
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(
                attrs={"placeholder": _("Name"), "class": "form-control"}
            )
        }

    def clean_status_name(self):
        name = self.cleaned_data["name"]
        if Statuses.objects.filter(name=name):
            raise forms.ValidationError(
                _("A task status with this name already exists.")
            )
        return name
