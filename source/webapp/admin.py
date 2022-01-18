from django.contrib import admin

# Register your models here.
from webapp.models import IssueModel, StatusModel, TypeModel


class IssueAdmin(admin.ModelAdmin):
    list_display = ['id', 'summary', 'description', 'created_at', 'updated_at']
    list_filter = ['created_at']
    search_fields = ['status', 'type']
    fields = ['summary', 'description', 'status', 'type', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(IssueModel, IssueAdmin)
admin.site.register(StatusModel)
admin.site.register(TypeModel)
