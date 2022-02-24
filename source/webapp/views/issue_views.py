from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, DetailView

# Create your views here.
from webapp.views.base_views import FormView as CustomFormView
from webapp.forms import IssueForm, SearchForm
from webapp.models import IssueModel, ProjectModel


class IssueListView(ListView):
    model = IssueModel
    context_object_name = 'issues'
    template_name = 'issue/issue_list.html'
    paginate_by = 10
    paginate_orphans = 0

    def get(self, request, *args, **kwargs):
        self.form = self.get_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(summary__icontains=self.search_value) | Q(description__icontains=self.search_value)
            queryset = queryset.filter(query)
            print(queryset)
        return queryset.order_by('-updated_at')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = SearchForm()
        if self.search_value:
            context['form'] = SearchForm(initial={'search': self.search_value})
            context['search'] = self.search_value
        return context

    def get_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data.get('search')


class IssueCreateView(PermissionRequiredMixin, CustomFormView):
    form_class = IssueForm
    template_name = 'issue/issue_create.html'
    permission_required = 'webapp.add_issue_in_own_project'

    def get_project(self):
        project_pk = self.request.POST.get("project")
        return get_object_or_404(ProjectModel, pk=project_pk)

    def has_permission(self):
        has_permission = super().has_permission()

        if self.request.method == "POST":
            has_permission = (
                    has_permission
                    and self.get_project().users.filter(pk=self.request.user.pk).exists()
            )
        return has_permission

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)

    def get_redirect_url(self):
        return redirect('webapp:issue_view', pk=self.object.pk)


class IssueDetailView(DetailView):
    template_name = 'issue/issue_view.html'
    model = IssueModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context


class IssueEditView(PermissionRequiredMixin, UpdateView):
    form_class = IssueForm
    template_name = 'issue/issue_edit.html'
    model = IssueModel
    permission_required = 'webapp.change_issue_in_own_project'

    def get_success_url(self):
        return reverse('webapp:issue_view', kwargs={'pk': self.object.pk})

    def has_permission(self):
        return (
            super().has_permission()
            and self.get_object().project.users.filter(pk=self.request.user.pk).exists()
        )


class IssueDeleteView(PermissionRequiredMixin, DeleteView):
    model = IssueModel
    template_name = 'issue/issue_delete.html'
    success_url = reverse_lazy('webapp:issue_list')
    permission_required = 'webapp.delete_issue_in_own_project'

    def has_permission(self):
        return (
                super().has_permission()
                and self.get_object().project.users.filter(pk=self.request.user.pk).exists()
        )

