from django.core.validators import MinLengthValidator
from django.db import models


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

    def __str__(self):
        return f"{self.pk}. {self.summary}, {self.type}, {self.status}."

    class Meta:
        db_table = 'issues'
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


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
