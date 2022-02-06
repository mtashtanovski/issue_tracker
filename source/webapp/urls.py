from django.urls import path

from webapp.views.project_views import IndexView, ProjectView, ProjectCreate
from webapp.views.issue_views import (IssueListView,
                                      IssueView,
                                      IssueCreate,
                                      IssueEdit,
                                      IssueDelete
                                      )

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('project/<int:pk>/', ProjectView.as_view(), name='project_view'),
    path('project/create/', ProjectCreate.as_view(), name='project_create'),

    path('issues/list', IssueListView.as_view(), name='issue_list'),
    path('issue/<int:pk>/view/', IssueView.as_view(template_name='issue/issue_view.html'), name='issue_view'),
    path('issue/create/', IssueCreate.as_view(), name='issue_create'),
    path('issue/<int:pk>/edit/', IssueEdit.as_view(), name='issue_edit'),
    path('issue/<int:pk>/delete/', IssueDelete.as_view(template_name='issue/issue_delete.html'), name='issue_delete')
]