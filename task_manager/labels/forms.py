from django import forms

from .models import Labels


class CreateUpdateLabelForm(forms.ModelForm):

    class Meta:
        model = Labels
        fields = ['label_name']
        widgets = {'name': forms.TextInput(attrs={'placeholder': 'Имя',
                                                  'class': 'form-control'})}

    def clean_label_name(self):
        label_name = self.cleaned_data['label_name']
        if Labels.objects.filter(label_name=label_name):
            raise forms.ValidationError('Label с таким Имя уже существует.')
        return label_name
