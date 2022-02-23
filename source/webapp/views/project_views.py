from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
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


class ProjectView(DetailView):
    template_name = 'project/project_view.html'
    model = ProjectModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        issues = self.object.issues.order_by('-created_at')
        context['issues'] = issues
        return context


class ProjectCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'webapp.add_projectmodel'
    model = ProjectModel
    form_class = ProjectForm
    template_name = 'project/project_create.html'

    def get_success_url(self):
        return reverse('webapp:project_view', kwargs={'pk': self.object.pk})
    
    def form_valid(self, form):
        response = super(ProjectCreate, self).form_valid(form)
        self.object.users.add(self.request.user)
        return response


class ProjectEdit(PermissionRequiredMixin, UpdateView):
    permission_required = 'webapp.change_projectmodel'
    form_class = ProjectForm
    template_name = 'project/project_edit.html'
    model = ProjectModel

    def get_success_url(self):
        return reverse('webapp:project_view', kwargs={'pk': self.object.pk})

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().user

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProjectDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'webapp.delete_projectmodel'
    model = ProjectModel
    template_name = 'project/project_delete.html'
    success_url = reverse_lazy('webapp:index')


class ChangeProjectUsers(UpdateView):
    model = ProjectModel
    template_name = 'project/change_users.html'
    form_class = ProjectUsersForm

    def get_success_url(self):
        return reverse('webapp:project_view', kwargs={'pk': self.object.pk})
