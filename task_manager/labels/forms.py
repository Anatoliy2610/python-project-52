from django import forms
from .models import Labels
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.core.exceptions import ValidationError


class CreateUpdateLabelForm(forms.ModelForm):

    class Meta:
        model = Labels
        fields = ['label_name']
        widgets = {'name': forms.TextInput(attrs={'placeholder': 'Имя',
                                                  'class': 'form-control'})}
        