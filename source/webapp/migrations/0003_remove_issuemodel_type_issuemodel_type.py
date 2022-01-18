# Generated by Django 4.0.1 on 2022-01-18 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_alter_issuemodel_status_alter_issuemodel_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issuemodel',
            name='type',
        ),
        migrations.AddField(
            model_name='issuemodel',
            name='type',
            field=models.ManyToManyField(blank=True, related_name='type', to='webapp.TypeModel', verbose_name='Тип'),
        ),
    ]
