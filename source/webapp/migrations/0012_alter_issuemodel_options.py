# Generated by Django 4.0.1 on 2022-02-24 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0011_alter_issuemodel_options_alter_projectmodel_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='issuemodel',
            options={'permissions': (('add_issue_in_own_project', 'Добавлять задачи в свой проект'), ('change_issue_in_own_project', 'Изменять задачи в своем проекте'), ('delete_issue_in_own_project', 'Удалять задачи в своем проекте')), 'verbose_name': 'Задача', 'verbose_name_plural': 'Задачи'},
        ),
    ]