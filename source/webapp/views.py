from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

# Create your views here.
from webapp.models import IssueModel
from django.views.generic import TemplateView
from webapp.forms import IssueForm


class IndexView(View):

    def get(self, request, *args, **kwargs):
        issues = IssueModel.objects.order_by('-updated_at')
        return render(request, 'index.html', {'issues': issues})


class IssueView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        issue = get_object_or_404(IssueModel, pk=kwargs.get("pk"))
        context['issue'] = issue
        return context


class IssueCreate(TemplateView):
    def get(self, request, *args, **kwargs):
        form = IssueForm()
        return render(request, 'issue_create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = IssueForm(data=request.POST)
        if form.is_valid():
            summary = form.cleaned_data.get('summary')
            description = form.cleaned_data.get('description')
            status = form.cleaned_data.get('status')
            type = form.cleaned_data.get('type')
            new_issue = IssueModel.objects.create(summary=summary, description=description, status=status,
                                                  type=type)
            return redirect('index')
        return render(request, 'issue_create.html', {'form': form})


class IssueEdit(TemplateView):

    def get(self, request, pk=None, *args, **kwargs):
        issue = get_object_or_404(IssueModel, pk=pk)
        form = IssueForm(initial={
            'summary': issue.summary,
            'description': issue.description,
            'status': issue.status,
            'type': issue.type
        })
        return render(request, 'issue_edit.html', {'issue': issue, 'form': form})

    def post(self, request, pk=None, *args, **kwargs):
        issue = get_object_or_404(IssueModel, pk=pk)
        form = IssueForm(data=request.POST)
        if form.is_valid():
            issue.summary = form.cleaned_data.get('summary')
            issue.description = form.cleaned_data.get('description')
            issue.status = form.cleaned_data.get('status')
            issue.type = form.cleaned_data.get('type')
            issue.save()
            return redirect('issue_view', pk=issue.pk)
        return render(request, 'issue_edit.html', {'issue': issue, 'form': form})


class IssueDelete(TemplateView):
    def get(self, request, pk=None, *args, **kwargs):
        issue = get_object_or_404(IssueModel, pk=pk)
        return render(request, 'issue_delete.html', {'issue': issue})

    def post(self, request, pk=None, *args, **kwargs):
        issue = get_object_or_404(IssueModel, pk=pk)
        issue.delete()
        return redirect('index')

