from django import forms

from .models import Labels


class CreateUpdateLabelForm(forms.ModelForm):

    class Meta:
        model = Labels
        fields = ['name']
        widgets = {'name': forms.TextInput(attrs={'placeholder': 'Имя',
                                                  'class': 'form-control'})}

    def clean_label_name(self):
        name = self.cleaned_data['name']
        if Labels.objects.filter(name=name):
            raise forms.ValidationError('Label с таким Имя уже существует.')
        return name
