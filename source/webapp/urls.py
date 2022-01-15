from django.urls import path

from webapp.views import (IndexView,
                          IssueView,
                          IssueCreate,
                          )

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('issue/<int:pk>/', IssueView.as_view(template_name='issue_view.html'), name='issue_view'),
    path('issue/create/', IssueCreate.as_view(template_name='issue_create.html'), name='issue_create')
]