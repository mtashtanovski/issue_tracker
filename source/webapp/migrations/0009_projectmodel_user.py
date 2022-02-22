# Generated by Django 4.0.1 on 2022-02-22 14:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0008_alter_projectmodel_finished_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectmodel',
            name='user',
            field=models.ManyToManyField(related_name='users', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
