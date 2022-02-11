from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.models import ProjectModel, IssueModel
from webapp.forms import ProjectForm


class IndexView(ListView):
    model = ProjectModel
    context_object_name = 'projects'
    template_name = 'project/index.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by("-started")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        return context


class ProjectView(DetailView):
    template_name = 'project/project_view.html'
    model = ProjectModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        issues = self.object.issues.order_by('-created_at')
        context['issues'] = issues
        print(context)
        return context


class ProjectCreate(LoginRequiredMixin, CreateView):
    model = ProjectModel
    form_class = ProjectForm
    template_name = 'project/project_create.html'

    def get_success_url(self):
        return reverse('webapp:project_view', kwargs={'pk': self.object.pk})


class ProjectEdit(LoginRequiredMixin, UpdateView):
    form_class = ProjectForm
    template_name = 'project/project_edit.html'
    model = ProjectModel

    def get_success_url(self):
        return reverse('webapp:project_view', kwargs={'pk': self.object.pk})


class ProjectDelete(LoginRequiredMixin, DeleteView):
    model = ProjectModel
    template_name = 'project/project_delete.html'
    success_url = reverse_lazy('webapp:index')