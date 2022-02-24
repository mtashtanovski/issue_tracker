from django.urls import path

from webapp.views.project_views import (IndexView,
                                        ProjectDetailView,
                                        ProjectCreateView,
                                        ProjectEditView,
                                        ProjectDeleteView,
                                        ChangeProjectUsersView
                                        )
from webapp.views.issue_views import (IssueListView,
                                      IssueDetailView,
                                      IssueCreateView,
                                      IssueEditView,
                                      IssueDeleteView
                                      )
app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project_view'),
    path('project/create/', ProjectCreateView.as_view(), name='project_create'),
    path('project/<int:pk>/edit/', ProjectEditView.as_view(), name='project_edit'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
    path('project/<int:pk>/change_users/', ChangeProjectUsersView.as_view(), name='chang_project_users'),

    path('issues/list', IssueListView.as_view(), name='issue_list'),
    path('issue/<int:pk>/', IssueDetailView.as_view(), name='issue_view'),
    path('issue/create/', IssueCreateView.as_view(), name='issue_create'),
    path('issue/<int:pk>/edit/', IssueEditView.as_view(), name='issue_edit'),
    path('issue/<int:pk>/delete/', IssueDeleteView.as_view(), name='issue_delete')
]