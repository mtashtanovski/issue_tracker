from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class IssueModel(models.Model):
    summary = models.CharField(max_length=200, null=False, blank=False, verbose_name="Заголовок",
                               validators=(MinLengthValidator(10),))
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name="Описание")
    status = models.ForeignKey('webapp.StatusModel', on_delete=models.PROTECT,
                               related_name='status', verbose_name="Статус")
    type = models.ManyToManyField('webapp.TypeModel', related_name='type', blank=True, verbose_name="Тип")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    project = models.ForeignKey('webapp.ProjectModel',
                                on_delete=models.CASCADE,
                                related_name='issues',
                                verbose_name="Проект",
                                null=True,
                                default=1)

    def __str__(self):
        return f"{self.pk}. {self.summary}, {self.type}, {self.status}."

    class Meta:
        db_table = 'issues'
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        permissions = (
            ("add_issue_in_own_project", "Добавлять задачи в свой проект"),
            ("change_issue_in_own_project", "Изменять задачи в своем проекте"),
            ("delete_issue_in_own_project", "Удалять задачи в своем проекте"),
        )


class StatusModel(models.Model):
    title = models.CharField(max_length=32, null=False, blank=False)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        db_table = 'statuses'
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class TypeModel(models.Model):
    title = models.CharField(max_length=32, null=False, blank=False)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        db_table = 'types'
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'


class ProjectModel(models.Model):
    title = models.CharField(max_length=50, blank=False, verbose_name="Название")
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name="Описание")
    started = models.DateField(null=False, blank=False, verbose_name="Дата начала")
    finished = models.DateField(null=True, blank=True, verbose_name="Дата окончания")
    users = models.ManyToManyField(User, related_name='projects', verbose_name="Пользователи проекта")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        db_table = 'projects'
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        permissions = (
            ("change_user_in_own_project", "Изменять список пользователей в своем проекте"),
        )
