from django import forms
from django.core.exceptions import ValidationError
from webapp.models import IssueModel, ProjectModel


class IssueForm(forms.ModelForm):
    class Meta:
        model = IssueModel
        exclude = []
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5, 'cols': 50}),
            'type': forms.CheckboxSelectMultiple()
        }

    def clean_summary(self):
        if len(self.cleaned_data.get('summary')) < 10:
            raise ValidationError(f"Название задачи должно быть более 10 символов!")
        return self.cleaned_data.get('summary')

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['description'] == cleaned_data['summary']:
            raise ValidationError(f"Описание задачи не должно повторять название!")
        return cleaned_data


class SearchForm(forms.Form):
    search = forms.CharField(max_length=30, required=False, label='Найти',
                             widget=forms.TextInput(attrs={'class': 'myfieldclass'}))


class ProjectForm(forms.ModelForm):
    class Meta:
        model = ProjectModel
        exclude = ('users',)
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5, 'cols': 50}),
        }


class ProjectUsersForm(forms.ModelForm):
    class Meta:
        model = ProjectModel
        fields = ('users',)
