from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, FormView

# Create your views here.
from webapp.base import FormView as CustomFormView
from webapp.forms import IssueForm
from webapp.models import IssueModel


class IndexView(View):
    def get(self, request, *args, **kwargs):
        issues = IssueModel.objects.order_by('-updated_at')
        return render(request, 'index.html', {'issues': issues})


class IssueCreate(CustomFormView):
    form_class = IssueForm
    template_name = 'issue_create.html'

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)

    def get_redirect_url(self):
        return redirect('issue_view', pk=self.object.pk)


class IssueView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        issue = get_object_or_404(IssueModel, pk=kwargs.get("pk"))
        context['issue'] = issue
        return context


class IssueEdit(FormView):
    form_class = IssueForm
    template_name = 'issue_edit.html'

    def dispatch(self, request, *args, **kwargs):
        self.issue = self.get_object()
        return super(IssueEdit, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issue'] = self.issue
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.issue
        return kwargs

    def form_valid(self, form):
        self.issue = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('issue_view', kwargs={"pk": self.issue.pk})

    def get_object(self):
        return get_object_or_404(IssueModel, pk=self.kwargs.get("pk"))


class IssueDelete(TemplateView):
    def get(self, request, pk=None, *args, **kwargs):
        issue = get_object_or_404(IssueModel, pk=pk)
        return render(request, 'issue_delete.html', {'issue': issue})

    def post(self, request, pk=None, *args, **kwargs):
        issue = get_object_or_404(IssueModel, pk=pk)
        issue.delete()
        return redirect('index')
