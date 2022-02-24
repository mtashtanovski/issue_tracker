from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.models import ProjectModel
from webapp.forms import ProjectForm, ProjectUsersForm


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


class ProjectDetailView(DetailView):
    template_name = 'project/project_view.html'
    model = ProjectModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        issues = self.object.issues.order_by('-created_at')
        context['issues'] = issues
        return context


class ProjectCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'webapp.add_projectmodel'
    model = ProjectModel
    form_class = ProjectForm
    template_name = 'project/project_create.html'

    def get_success_url(self):
        return reverse('webapp:project_view', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        response = super(ProjectCreateView, self).form_valid(form)
        self.object.users.add(self.request.user)
        return response


class ProjectEditView(PermissionRequiredMixin, UpdateView):
    form_class = ProjectForm
    template_name = 'project/project_edit.html'
    model = ProjectModel
    permission_required = 'webapp.change_projectmodel'

    def get_success_url(self):
        return reverse('webapp:project_view', kwargs={'pk': self.object.pk})


class ProjectDeleteView(PermissionRequiredMixin, DeleteView):
    model = ProjectModel
    template_name = 'project/project_delete.html'
    success_url = reverse_lazy('webapp:index')
    permission_required = 'webapp.delete_projectmodel'


class ChangeProjectUsersView(PermissionRequiredMixin, UpdateView):
    model = ProjectModel
    template_name = 'project/change_users.html'
    form_class = ProjectUsersForm
    permission_required = 'webapp.change_user_in_own_project'

    def get_success_url(self):
        return reverse('webapp:project_view', kwargs={'pk': self.object.pk})

    def has_permission(self):
        return (
                super().has_permission()
                and self.get_object().users.filter(pk=self.request.user.pk).exists()
        )
