from django.shortcuts import render, get_object_or_404
from django.views import View

# Create your views here.
from webapp.models import IssueModel
from django.views.generic import TemplateView


class IndexView(View):

    def get(self, request, *args, **kwargs):
        issues = IssueModel.objects.order_by('updated_at')
        return render(request, 'index.html', {'issues': issues})


class IssueView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        issue = get_object_or_404(IssueModel, pk=kwargs.get("pk"))
        context['issue'] = issue
        return context
