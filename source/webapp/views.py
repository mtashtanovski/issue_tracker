from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

# Create your views here.
from webapp.models import IssueModel
from django.views.generic import TemplateView
from webapp.forms import IssueForm
from webapp.base import FormView as CustomView


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


class IssueCreate(CustomView):
    form_class = IssueForm
    template_name = 'issue_create.html'

    def form_valid(self, form):
        type = form.cleaned_data.pop('type')
        self.object = IssueModel.objects.create(**form.cleaned_data)
        self.object.type.set(type)
        return super().form_valid(form)

    def get_redirect_url(self):
        return redirect('issue_view', pk=self.object.pk)

    # def get(self, request, *args, **kwargs):
    #     form = IssueForm()
    #     return render(request, 'issue_create.html', {'form': form})
    #
    # def post(self, request, *args, **kwargs):
    #     form = IssueForm(data=request.POST)
    #     if form.is_valid():
    #         # summary = form.cleaned_data.get('summary')
    #         # description = form.cleaned_data.get('description')
    #         # status = form.cleaned_data.get('status')
    #         type = form.cleaned_data.pop('type')
    #         new_issue = IssueModel.objects.create(**form.cleaned_data)
    #         new_issue.type.set(type)
    #         return redirect('issue_view', pk=new_issue.pk)
    #     return render(request, 'issue_create.html', {'form': form})


class IssueEdit(TemplateView):

    def get(self, request, pk=None, *args, **kwargs):
        issue = get_object_or_404(IssueModel, pk=pk)
        form = IssueForm(initial={
            'summary': issue.summary,
            'description': issue.description,
            'status': issue.status,
            'type': issue.type.all()
        })
        return render(request, 'issue_edit.html', {'issue': issue, 'form': form})

    def post(self, request, pk=None, *args, **kwargs):
        issue = get_object_or_404(IssueModel, pk=pk)
        form = IssueForm(data=request.POST)
        if form.is_valid():
            type = form.cleaned_data.pop('type')
            issue.type.set(type)
            issue.summary = form.cleaned_data.get('summary')
            issue.description = form.cleaned_data.get('description')
            issue.status = form.cleaned_data.get('status')
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

