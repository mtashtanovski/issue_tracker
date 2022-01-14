from django import forms
from django.forms import widgets
from webapp.models import IssueModel, TypeModel, StatusModel


class IssueForm(forms.Form):
    summary = forms.CharField(max_length=200, required=True, label="Заголовок:")
    description = forms.CharField(max_length=2000, required=False, label="Описание:",
                                  widget=widgets.Textarea(attrs={'rows': 5, 'cols': 50}))
    status = forms.ModelChoiceField(queryset=TypeModel.objects.all(), label="Статус:")
    type = forms.ModelChoiceField(queryset=StatusModel.objects.all(), label="Тип задачи:")
