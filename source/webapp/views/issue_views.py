from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import TemplateView, FormView, ListView

# Create your views here.
from webapp.views.base_views import FormView as CustomFormView
from webapp.forms import IssueForm, SearchForm
from webapp.models import IssueModel


# class IndexView(View):
#     def get(self, request, *args, **kwargs):
#         issues = IssueModel.objects.order_by('-updated_at')
#         return render(request, 'issue_list.html', {'issues': issues})

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


class IssueCreate(CustomFormView):
    form_class = IssueForm
    template_name = 'issue/issue_create.html'

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
    template_name = 'issue/issue_edit.html'

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
        return render(request, 'issue/issue_delete.html', {'issue': issue})

    def post(self, request, pk=None, *args, **kwargs):
        issue = get_object_or_404(IssueModel, pk=pk)
        issue.delete()
        return redirect('index')
