from django.shortcuts import render
from django.views import View

# Create your views here.
from webapp.models import IssueModel


class IndexView(View):
    def get(self, request, *args, **kwargs):
        issues = IssueModel.objects.order_by('updated_at')
        return render(request, 'index.html', {'issues': issues})
