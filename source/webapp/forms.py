from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets
from webapp.models import IssueModel, TypeModel, StatusModel, ProjectModel


class IssueForm(forms.ModelForm):
    # summary = forms.CharField(max_length=200, required=True, label="Заголовок:")
    # description = forms.CharField(max_length=2000, required=False, label="Описание:",
    #                               widget=widgets.Textarea(attrs={'rows': 5, 'cols': 50}))
    # status = forms.ModelChoiceField(queryset=StatusModel.objects.all(), label="Статус:")
    # # type = forms.ModelChoiceField(queryset=TypeModel.objects.all(), label="Тип задачи:")
    # type = forms.ModelMultipleChoiceField(required=False, label='Тип задачи:',
    #                                       queryset=TypeModel.objects.all(),
    #                                       widget=forms.CheckboxSelectMultiple())
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
        exclude = []
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5, 'cols': 50}),
        }
