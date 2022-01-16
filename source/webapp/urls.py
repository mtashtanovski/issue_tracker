from django.urls import path

from webapp.views import (IndexView,
                          IssueView,
                          IssueCreate,
                          IssueEdit,
                          IssueDelete
                          )

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('issue/<int:pk>/view/', IssueView.as_view(template_name='issue_view.html'), name='issue_view'),
    path('issue/create/', IssueCreate.as_view(template_name='issue_create.html'), name='issue_create'),
    path('issue/<int:pk>/edit/', IssueEdit.as_view(template_name='issue_edit.html'), name='issue_edit'),
    path('issue/<int:pk>/delete/', IssueDelete.as_view(template_name='issue_delete.html'), name='issue_delete')
]