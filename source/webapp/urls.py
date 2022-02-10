from django.urls import path

from webapp.views.project_views import (IndexView,
                                        ProjectView,
                                        ProjectCreate,
                                        ProjectEdit,
                                        ProjectDelete
                                        )
from webapp.views.issue_views import (IssueListView,
                                      IssueView,
                                      IssueCreate,
                                      IssueEdit,
                                      IssueDelete
                                      )
app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('project/<int:pk>/', ProjectView.as_view(), name='project_view'),
    path('project/create/', ProjectCreate.as_view(), name='project_create'),
    path('project/<int:pk>/edit/', ProjectEdit.as_view(), name='project_edit'),
    path('project/<int:pk>/delete/', ProjectDelete.as_view(), name='project_delete'),

    path('issues/list', IssueListView.as_view(), name='issue_list'),
    path('issue/<int:pk>/', IssueView.as_view(), name='issue_view'),
    path('issue/create/', IssueCreate.as_view(), name='issue_create'),
    path('issue/<int:pk>/edit/', IssueEdit.as_view(), name='issue_edit'),
    path('issue/<int:pk>/delete/', IssueDelete.as_view(), name='issue_delete')
]